# Validated extraction method (v3) — 2026-08-25

Per vendor: navigate to `google.com/search?q=<vendor>`, then run the JS below.
Poll ~5s; the Knowledge Panel right rail renders late.

## Three bugs found and fixed during Phase 0/1

1. **Race** — running JS immediately after `navigate` reads the DOM before the
   Knowledge Panel renders. Fixed by polling inside the JS (top-level `await` works).
2. **`img > 2` discriminator** — used to tell the KP carousel apart from the footer
   related-searches block. Fails because tile logos lazy-load below the fold.
   Fixed by also accepting any block inside an ancestor with class `TQc1id`
   (the Knowledge Panel container).
3. **`innerText` returns empty strings** (THE COSTLY ONE) — the carousel tile
   anchors are empty `<a>` elements; the visible names live in *sibling* leaf
   nodes, and `innerText` is layout-dependent so it returns '' for the
   horizontally-scrolled, off-screen tiles. This silently produced `peers: []`
   for exactly the vendors that DO have carousels. Fixed by reading `textContent`
   from leaf descendants of the block.

## Working extractor

```js
await (async()=>{
  const s=m=>new Promise(r=>setTimeout(r,m));
  const g=()=>{
    const L=[...document.querySelectorAll('*')].filter(e=>!e.children.length
      &&/^People also search for$/i.test(e.textContent.trim()));
    for(const h of L){
      let c=h,box=null,kp=false;
      for(let i=0;i<8&&c;i++){
        c=c.parentElement; if(!c)break;
        if(!box&&c.querySelectorAll('a').length>2)box=c;
        if(/TQc1id|kp-wholepage/i.test((c.className||'').toString()))kp=true;
      }
      if(box&&(kp||box.querySelectorAll('img').length>2))return box;
    }
    return null;
  };
  let b=null;
  for(let i=0;i<12;i++){b=g();if(b)break;await s(400)}
  const d=document.body.innerText;
  return JSON.stringify({
    co:/Source:\s*Wikipedia|Headquarters|Date founded/.test(d),
    p:b?[...new Set([...b.querySelectorAll('*')]
        .filter(e=>e.children.length===0&&e.textContent.trim())
        .map(e=>e.textContent.trim().replace(/\s+/g,' '))
        .filter(t=>t.length<60&&!/^People also search for$|^See more$|^Trending$/i.test(t)))]:[]
  });
})()
```

To get the full ~25-name list instead of the 4 visible tiles: click the block's
"See more" anchor, wait ~3s (it navigates), then re-extract. Costs a second
round trip per vendor.

## Operational limits hit

- `browser_batch` times out past ~10-12 actions; **output is discarded
  all-or-nothing** on timeout, so a timed-out batch must be fully re-run.
  Reliable size: 3-4 vendors per batch (2 actions each).
- The Chrome extension disconnected once mid-run and had to be re-attached.
- Returning `innerHTML` or anything containing URLs trips a
  `[BLOCKED: Cookie/query string data]` guard. Return only extracted text.

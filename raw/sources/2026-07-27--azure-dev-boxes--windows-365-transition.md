# Microsoft Dev Box closed to new customers 2025-11-01; maintenance mode; capabilities folded into Windows 365

- URLs:
  - https://azure.microsoft.com/en-us/products/dev-box (Microsoft Azure product
    page) — **primary**; carries the transition banner
  - https://learn.microsoft.com/en-us/azure/dev-box/dev-box-windows-365-announcement
    (Microsoft Learn, "Microsoft Dev Box - maintenance mode"; canonical URL
    `/azure/dev-box/dev-box-roadmap`; `ms.date` 2026-05-01, page updated
    2026-05-04) — **primary**; the roadmap page was converted into the
    maintenance-mode notice
  - https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/
    (Windows Developer Blog, Build 2026, published 2026-06-02) — **primary** for
    what actually shipped on the Windows 365 side
  - https://www.directionsonmicrosoft.com/in-brief/dev-box-merges-into-windows-365/
    (Directions on Microsoft) — independent licensing analysis
  - https://www.licensingschool.co.uk/licensing-blog/2025/11/04/dev-box-capabilities-coming-to-windows-365/
    and https://www.licensingschool.co.uk/licensing-blog/2026/07/01/windows-365-and-developers/
    (Licensing Lore & Law, 2025-11-04 and 2026-07-01) — independent licensing
    analysis
- Fetched: 2026-07-27
- Good for: confirming that Dev Box is closed to new sign-ups (2025-11-01) and in
  maintenance mode; establishing that this is a **capability merge into Windows
  365, not a rename**; identifying the successor shapes (Windows 365 with
  Developer configuration; Windows 365 for Agents); and flagging that the Dev Box
  end-of-service date is **not yet announced**.

## Facts

### The banner on the Azure product page (primary)

Verbatim, from `https://azure.microsoft.com/en-us/products/dev-box`:

> "Capabilities of Microsoft Dev Box are transitioning to Windows 365. Existing
> customers can continue using Dev Box, but new sign-ups will no longer be
> accepted as of November 1, 2025."

The page directs readers to "Learn more about Windows 365." The Dev Box product
page itself is still live and still Microsoft-branded — no redirect.

### Maintenance mode (primary, Microsoft Learn)

The Dev Box **roadmap** page has been replaced in place by a maintenance-mode
notice. Verbatim:

> "Dev Box is now in maintenance mode, with no additional features planned.
> Microsoft's investments for developer cloud environments are focused on
> Windows 365, which provides a unified, scalable solution for developer
> scenarios."

> "Customers should consider Windows 365 as the recommended path forward for
> virtualized developer environments. Dev Box will remain supported for existing
> usage, and guidance will be provided to help customers transition."

Microsoft's own four bullets under "What this means for you":

- **Existing deployments continue to work.** "Your current dev boxes, pools, and
  configurations remain fully functional and supported."
- **No new features will ship.** Previously planned capabilities won't reach GA.
- **Windows 365 is the path forward.**
- Transition guidance and resources to follow, "at a pace that works for your
  organization."

Features explicitly killed before GA (useful as evidence the freeze is real, and
because several were governance features):

- Enterprise management: **on-behalf creation**, **firewall Service Tags**
  (traffic rules by Service Tag), **developer offboarding** (auto-deprovision on
  leaver/transfer).
- Performance & reliability: **SSO for existing dev box machines**, auto
  remediation improvements, latency improvements.
- Retired preview: **guest account access** via Entra B2B.

Note for the wiki's purposes: firewall Service Tags and automatic developer
offboarding are egress-control and joiner-mover-leaver features — i.e. exactly
the governance gaps a regulated buyer would have been waiting on. They are not
coming.

### **No end-of-service date has been announced.**

Neither Microsoft source states when Dev Box stops running. Directions on
Microsoft reports the end date as TBD and says Microsoft is encouraging existing
customers to "participate in previews of the merged Windows 365–Dev Box service
so they can move quickly when Microsoft announces the end date for the current
Dev Box." Treat any specific retirement date as unknown, not as "indefinite."

### This is a merge, not a rename

Dev Box was **already built on the Windows 365 / Cloud PC platform** — the change
retires the separately-branded Azure service and consolidates its developer
capabilities into the Windows 365 product line, which has its own SKUs,
licensing, and admin surface (Intune / Microsoft 365 admin center rather than the
Azure Dev Center resource model). Directions on Microsoft characterizes it as "a
**capability merge** rather than a simple rename."

Consequence for the wiki: **"Windows 365" is not an `aka` for Dev Box.** It is a
distinct, pre-existing, still-sold Microsoft product that absorbs the capability.

### What on the Windows 365 side replaces it (primary, Build 2026, 2026-06-02)

Two distinct things, both announced at Build 2026:

1. **Windows 365 with Developer configuration** — *public preview* as of
   2026-06-02. Verbatim: "Windows 365 with Developer configuration offers
   ready-to-code environments in the cloud. This image provides a consistent,
   preconfigured Windows 11 development experience from first sign-in, with
   commonly used tools such as Visual Studio Code, Git, GitHub CLI and WSL
   already set up." Extensible with additional SDKs/CLIs; stays under
   organizational policy. This is the direct functional successor to a Dev Box
   pool image.

2. **Windows 365 for Agents** — *generally available*, delivered within **Agent
   365**. Verbatim: "Windows 365 for Agents provides Cloud PCs that enable AI
   agents to execute multi-step workflows across software, including opening
   apps, navigating interfaces, entering inputs and processing data." Agents run
   in Intune-managed Cloud PCs kept fully separate from the user's own machine —
   i.e. it is positioned as a **containment boundary for computer-using agents**,
   extending Microsoft's execution-container model beyond the local device.

The second item is the more interesting one for this wiki: the successor product
line has an explicit, separately-branded agent-sandboxing SKU, which Dev Box
never had. Note the status asymmetry — the *developer* image is preview, the
*agent* Cloud PC is GA.

### Licensing (third-party analysis, **not** confirmed by a Microsoft source)

Multiple independent licensing analysts (Directions on Microsoft; Licensing Lore
& Law, 2025-11-04) report that the developer capabilities in Windows 365 are
"enabled with **Windows 365 Frontline**," and that Frontline carries roughly a
**50% premium over Windows 365 Enterprise** but lets one license cover **up to
three Cloud PCs** per user (intended for shift/timezone patterns).

Neither Microsoft page fetched states a required SKU. Treat the Frontline
requirement and the pricing delta as **analyst reporting, medium confidence** —
cite it as such and do not promote it into frontmatter.

### Onboarding exception process

Licensing Lore & Law (2025-11-04) reports that organizations that had already
tested or evaluated Dev Box before the 2025-11-01 cutoff **can request an
exception** to onboard afterwards, via a form linked from Microsoft's
announcement. Not restated on either Microsoft page fetched — medium confidence.
Practical read: the door is shut for a genuinely new buyer, and ajar only for
someone with a pre-existing evaluation.

## Assessment

- **No ownership change.** Still a first-party Microsoft service; `ownership_state`
  stays `public`. This is a product sunset/consolidation, not M&A.
- The repo already has a precedent for expressing frozen-product status without
  destroying the ownership fact: `wiki/vendors/helicone.md` carries
  `ownership_state: acquired-closed` plus a `maintenance-mode` **tag**. Same
  treatment applies here.
- **Buying relevance is what changed.** A hedge-fund CTO reading this wiki today
  cannot buy Dev Box. The page must lead with that, and point at Windows 365
  (Developer configuration / for Agents) as where to look instead.
- No Windows 365 vendor page exists in `wiki/vendors/` as of 2026-07-27.

"""Ninety 9 Bottles – Streamlit App"""

import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ninety 9 Bottles | Beer, Wine & Spirits – Fairfield County, CT",
    page_icon="🍺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Global ──────────────────────────────────────────── */
    :root {
      --dark-bg: #1a1a2e;
      --primary: #c8a96e;
      --primary-dark: #a07840;
      --text-light: #f0ece4;
      --text-muted: #b0a89a;
      --card-bg: #ffffff;
      --section-alt: #f8f5f0;
      --border: #e0d6c8;
      --shadow: 0 4px 20px rgba(0,0,0,.12);
      --shadow-lg: 0 8px 40px rgba(0,0,0,.18);
    }

    html, body, [data-testid="stAppViewContainer"] {
      font-family: 'Georgia', 'Times New Roman', serif;
      color: #2c2c2c;
      background: #ffffff;
    }

    /* Hide default Streamlit chrome that clutters the view */
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stToolbar"] { display: none; }
    .block-container { padding-top: 0 !important; max-width: 100% !important; }

    /* ── Navbar ──────────────────────────────────────────── */
    .n9b-nav {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(26,26,46,.97);
      backdrop-filter: blur(6px);
      padding: 0 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 70px;
      box-shadow: 0 2px 12px rgba(0,0,0,.3);
    }
    .n9b-nav-brand {
      display: flex;
      align-items: center;
      gap: .6rem;
      text-decoration: none;
    }
    .n9b-nav-num {
      font-family: Georgia, serif;
      font-size: 2rem;
      font-weight: bold;
      color: var(--primary);
      line-height: 1;
    }
    .n9b-nav-label {
      font-size: .75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: .12em;
      line-height: 1.3;
      font-family: Arial, sans-serif;
    }
    .n9b-nav-links {
      display: flex;
      gap: 2rem;
      list-style: none;
      margin: 0; padding: 0;
    }
    .n9b-nav-links a {
      color: var(--text-light);
      text-decoration: none;
      font-family: Arial, sans-serif;
      font-size: .85rem;
      text-transform: uppercase;
      letter-spacing: .1em;
    }
    .n9b-nav-links a:hover { color: var(--primary); }

    /* ── Hero ────────────────────────────────────────────── */
    .n9b-hero {
      background: linear-gradient(135deg,#1a1a2e 0%,#16213e 40%,#0f3460 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 6rem 2rem 5rem;
      position: relative;
      overflow: hidden;
    }
    .n9b-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(ellipse at 50% 60%,rgba(200,169,110,.12) 0%,transparent 70%);
    }
    .n9b-hero-content { position: relative; max-width: 780px; margin: 0 auto; }
    .n9b-eyebrow {
      font-family: Arial, sans-serif;
      font-size: .8rem;
      text-transform: uppercase;
      letter-spacing: .25em;
      color: var(--primary);
      margin-bottom: 1.2rem;
    }
    .n9b-hero-title {
      font-size: clamp(3rem,8vw,5.5rem);
      font-weight: bold;
      color: var(--text-light);
      line-height: 1;
      margin-bottom: .4rem;
    }
    .n9b-hero-title span { color: var(--primary); }
    .n9b-subtitle {
      font-family: Arial, sans-serif;
      font-size: 1.1rem;
      color: var(--text-muted);
      margin-bottom: 2.5rem;
      letter-spacing: .05em;
    }
    .n9b-desc {
      font-size: 1.1rem;
      color: var(--text-light);
      opacity: .85;
      max-width: 560px;
      margin: 0 auto 2.5rem;
    }
    .n9b-hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
    .n9b-btn {
      display: inline-block;
      padding: .85rem 2.4rem;
      border-radius: 3px;
      font-family: Arial, sans-serif;
      font-size: .85rem;
      text-transform: uppercase;
      letter-spacing: .15em;
      text-decoration: none;
      cursor: pointer;
    }
    .n9b-btn-primary {
      background: var(--primary);
      color: #1a1a2e;
      font-weight: bold;
    }
    .n9b-btn-outline {
      background: transparent;
      border: 2px solid var(--primary);
      color: var(--primary);
    }

    /* ── Section common ──────────────────────────────────── */
    .n9b-section { padding: 5rem 2rem; }
    .n9b-section-alt { background: var(--section-alt); }
    .n9b-section-header {
      text-align: center;
      max-width: 680px;
      margin: 0 auto 3.5rem;
    }
    .n9b-section-label {
      font-family: Arial, sans-serif;
      font-size: .75rem;
      text-transform: uppercase;
      letter-spacing: .2em;
      color: var(--primary-dark);
      display: block;
      margin-bottom: .8rem;
    }
    .n9b-section-title {
      font-size: clamp(1.8rem,4vw,2.6rem);
      color: #1a1a2e;
      line-height: 1.25;
      margin-bottom: 1rem;
    }
    .n9b-section-desc { color: #555; font-size: 1.05rem; line-height: 1.7; }

    /* ── Features grid ───────────────────────────────────── */
    .n9b-features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
      gap: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }
    .n9b-feature-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 2rem 1.5rem;
      text-align: center;
      box-shadow: var(--shadow);
    }
    .n9b-feature-icon { font-size: 2.4rem; margin-bottom: 1rem; }
    .n9b-feature-card h3 { font-size: 1.1rem; color: #1a1a2e; margin-bottom: .6rem; }
    .n9b-feature-card p {
      font-size: .92rem;
      color: #666;
      line-height: 1.6;
      font-family: Arial, sans-serif;
    }

    /* ── Locations grid ──────────────────────────────────── */
    .n9b-locations-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit,minmax(300px,1fr));
      gap: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }
    .n9b-location-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      box-shadow: var(--shadow);
    }
    .n9b-location-header {
      background: var(--dark-bg);
      padding: 1.5rem;
      text-align: center;
    }
    .n9b-location-city {
      font-size: 1.4rem;
      color: var(--primary);
      font-weight: bold;
      margin-bottom: .2rem;
    }
    .n9b-location-tag {
      font-family: Arial, sans-serif;
      font-size: .72rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: .15em;
    }
    .n9b-location-body { padding: 1.8rem; }
    .n9b-location-info { display: flex; flex-direction: column; gap: 1rem; font-family: Arial, sans-serif; }
    .n9b-location-row { display: flex; gap: .8rem; align-items: flex-start; }
    .n9b-location-icon { font-size: 1.1rem; flex-shrink: 0; margin-top: 2px; }
    .n9b-location-text { flex: 1; }
    .n9b-location-text strong {
      display: block;
      font-size: .75rem;
      text-transform: uppercase;
      letter-spacing: .1em;
      color: #999;
      margin-bottom: .2rem;
    }
    .n9b-location-text a { color: #333; text-decoration: none; font-size: .95rem; }
    .n9b-location-text a:hover { color: var(--primary-dark); }
    .n9b-location-hours { font-size: .9rem; color: #444; }
    .n9b-location-hours span { color: #777; font-size: .82rem; }
    .n9b-map-btn {
      display: block;
      margin-top: 1.5rem;
      padding: .7rem;
      background: var(--dark-bg);
      color: var(--primary);
      text-align: center;
      text-decoration: none;
      font-family: Arial, sans-serif;
      font-size: .8rem;
      text-transform: uppercase;
      letter-spacing: .12em;
      border-radius: 4px;
    }
    .n9b-map-btn:hover { background: var(--primary); color: var(--dark-bg); }

    /* ── Hours banner ────────────────────────────────────── */
    .n9b-hours-banner {
      background: var(--dark-bg);
      color: var(--text-light);
      padding: 3.5rem 2rem;
      text-align: center;
    }
    .n9b-hours-banner h2 { font-size: 1.8rem; color: var(--primary); margin-bottom: .5rem; }
    .n9b-hours-banner > p {
      font-family: Arial, sans-serif;
      font-size: .95rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }
    .n9b-hours-table {
      font-family: Arial, sans-serif;
      font-size: 1rem;
      border-collapse: collapse;
      max-width: 380px;
      width: 100%;
      margin: 0 auto;
    }
    .n9b-hours-table td { padding: .55rem 1.5rem; border-bottom: 1px solid rgba(255,255,255,.07); }
    .n9b-hours-table td:first-child { text-align: left; color: var(--text-muted); }
    .n9b-hours-table td:last-child { text-align: right; color: var(--text-light); font-weight: bold; }

    /* ── Gallery / Photos ────────────────────────────────── */
    .n9b-gallery { background: #ffffff; text-align: center; }
    .n9b-gallery-cta { display: flex; flex-direction: column; align-items: center; gap: 1.5rem; }
    .n9b-gallery-icon { font-size: 4rem; line-height: 1; }
    .n9b-gallery-btn {
      display: inline-block;
      padding: 1rem 2.8rem;
      background: var(--primary);
      color: #1a1a2e;
      font-family: Arial, sans-serif;
      font-size: .9rem;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: .15em;
      text-decoration: none;
      border-radius: 3px;
    }
    .n9b-gallery-btn:hover { background: var(--primary-dark); }

    /* ── Social ──────────────────────────────────────────── */
    .n9b-social-links { display: flex; justify-content: center; margin-top: 2rem; }
    .n9b-social-fb {
      display: inline-flex;
      align-items: center;
      gap: .6rem;
      padding: .8rem 1.8rem;
      border-radius: 4px;
      background: #1877F2;
      color: #ffffff;
      font-family: Arial, sans-serif;
      font-size: .9rem;
      font-weight: bold;
      text-decoration: none;
    }
    .n9b-social-fb:hover { background: #1565d8; }

    /* ── Footer ──────────────────────────────────────────── */
    .n9b-footer {
      background: #0f0f1e;
      color: var(--text-muted);
      padding: 3rem 2rem 2rem;
      text-align: center;
      font-family: Arial, sans-serif;
    }
    .n9b-footer-logo {
      font-size: 2rem;
      color: var(--primary);
      font-family: Georgia, serif;
      font-weight: bold;
      margin-bottom: .4rem;
    }
    .n9b-footer-tagline {
      font-size: .8rem;
      text-transform: uppercase;
      letter-spacing: .18em;
      color: #555;
      margin-bottom: 2rem;
    }
    .n9b-footer-locs {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 2rem;
      margin-bottom: 2rem;
      font-size: .85rem;
    }
    .n9b-footer-locs strong { display: block; color: var(--primary); margin-bottom: .3rem; }
    .n9b-footer-locs a { color: inherit; }
    .n9b-footer-divider {
      border: none;
      border-top: 1px solid #222;
      margin: 1.5rem auto;
      max-width: 500px;
    }
    .n9b-footer-copy { font-size: .78rem; color: #444; }

    /* ── Age Gate ────────────────────────────────────────── */
    .n9b-age-gate-page {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(10,10,20,.97);
      padding: 2rem 1rem;
    }
    .n9b-age-box {
      background: var(--dark-bg);
      border: 1px solid var(--primary);
      border-radius: 8px;
      padding: 3rem 2.5rem;
      max-width: 480px;
      width: 100%;
      text-align: center;
    }
    .n9b-age-logo {
      font-size: 3rem;
      color: var(--primary);
      font-family: Georgia, serif;
      font-weight: bold;
      line-height: 1;
      margin-bottom: .2rem;
    }
    .n9b-age-brand {
      font-family: Arial, sans-serif;
      font-size: .72rem;
      text-transform: uppercase;
      letter-spacing: .2em;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }
    .n9b-age-box h2 { color: var(--text-light); font-size: 1.3rem; margin-bottom: .8rem; }
    .n9b-age-box p {
      font-family: Arial, sans-serif;
      color: var(--text-muted);
      font-size: .9rem;
      margin-bottom: 2rem;
    }

    /* Streamlit button overrides for age gate */
    div[data-testid="stVerticalBlock"] .stButton > button {
      border-radius: 3px;
      font-family: Arial, sans-serif;
      font-size: .85rem;
      text-transform: uppercase;
      letter-spacing: .15em;
      padding: .85rem 2.4rem;
      width: 100%;
    }

    @media (max-width: 768px) {
      .n9b-nav-links { display: none; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Session state ─────────────────────────────────────────────────────────────
if "age_verified" not in st.session_state:
    st.session_state.age_verified = False

# ── Age Verification Gate ─────────────────────────────────────────────────────
if not st.session_state.age_verified:
    st.markdown(
        '<div class="n9b-age-gate-page">',
        unsafe_allow_html=True,
    )
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown(
            """
            <div class="n9b-age-box">
              <div class="n9b-age-logo">99</div>
              <div class="n9b-age-brand">Ninety 9 Bottles · Fairfield County, CT</div>
              <h2>Are you 21 or older?</h2>
              <p>You must be of legal drinking age to enter this website.
                 Please verify your age to continue.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("✅  Yes, I'm 21+", use_container_width=True, type="primary"):
            st.session_state.age_verified = True
            st.rerun()
        st.link_button(
            "🚪  No, exit",
            "https://www.responsibility.org/",
            use_container_width=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ── Navigation ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <nav class="n9b-nav">
      <a href="#home" class="n9b-nav-brand">
        <span class="n9b-nav-num">99</span>
        <span class="n9b-nav-label">Ninety 9 Bottles<br>Fairfield County, CT</span>
      </a>
      <ul class="n9b-nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#locations">Locations</a></li>
        <li><a href="#hours">Hours</a></li>
        <li><a href="#photos">Photos</a></li>
        <li><a href="#social">Follow Us</a></li>
      </ul>
    </nav>
    """,
    unsafe_allow_html=True,
)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <section class="n9b-hero" id="home">
      <div class="n9b-hero-content">
        <p class="n9b-eyebrow">Fairfield County's Favorite Bottle Shop</p>
        <h1 class="n9b-hero-title"><span>Ninety 9</span><br>Bottles</h1>
        <p class="n9b-subtitle">Beer &bull; Wine &bull; Spirits</p>
        <p class="n9b-desc">
          Your locally owned neighborhood bottle shop—three convenient locations
          across Fairfield County with an expertly curated selection and
          friendly, knowledgeable staff.
        </p>
        <div class="n9b-hero-btns">
          <a href="#locations" class="n9b-btn n9b-btn-primary">Find a Location</a>
          <a href="#about" class="n9b-btn n9b-btn-outline">About Us</a>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ── About / Features ──────────────────────────────────────────────────────────
st.markdown(
    """
    <section class="n9b-section n9b-section-alt" id="about">
      <div class="n9b-section-header">
        <span class="n9b-section-label">Why Ninety 9 Bottles?</span>
        <h2 class="n9b-section-title">Your Local Bottle Shop, Three Locations Strong</h2>
        <p class="n9b-section-desc">
          Ninety 9 Bottles is a locally owned and operated bottle shop serving Fairfield County
          since the beginning. We pride ourselves on a handpicked selection, fair prices,
          and a team that genuinely loves what they do.
        </p>
      </div>
      <div class="n9b-features-grid">
        <div class="n9b-feature-card">
          <div class="n9b-feature-icon">🍺</div>
          <h3>Craft Beer Haven</h3>
          <p>An outstanding rotating selection of local, regional, and hard-to-find craft beers that keeps enthusiasts coming back.</p>
        </div>
        <div class="n9b-feature-card">
          <div class="n9b-feature-icon">🍷</div>
          <h3>Wine for Every Palate</h3>
          <p>From everyday bottles to special-occasion finds, our wine section covers every style, region, and price point.</p>
        </div>
        <div class="n9b-feature-card">
          <div class="n9b-feature-icon">🥃</div>
          <h3>Premium Spirits</h3>
          <p>Whiskey, bourbon, gin, rum, tequila, and more—curated with care and priced competitively.</p>
        </div>
        <div class="n9b-feature-card">
          <div class="n9b-feature-icon">🎉</div>
          <h3>Tastings &amp; Events</h3>
          <p>We regularly host in-store tastings so you can discover your next favorite before you buy.</p>
        </div>
        <div class="n9b-feature-card">
          <div class="n9b-feature-icon">🤝</div>
          <h3>Expert Staff</h3>
          <p>Our passionate team is always ready to help you find the perfect bottle for any occasion or budget.</p>
        </div>
        <div class="n9b-feature-card">
          <div class="n9b-feature-icon">🏘️</div>
          <h3>Community Roots</h3>
          <p>Locally owned and deeply connected to the Fairfield County community—we treat every customer like a neighbor.</p>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ── Locations ─────────────────────────────────────────────────────────────────
st.markdown(
    """
    <section class="n9b-section" id="locations">
      <div class="n9b-section-header">
        <span class="n9b-section-label">Three Convenient Locations</span>
        <h2 class="n9b-section-title">Find Your Nearest Ninety 9 Bottles</h2>
        <p class="n9b-section-desc">
          All three of our Fairfield County locations offer the same great selection and service,
          with plenty of free parking at each site.
        </p>
      </div>
      <div class="n9b-locations-grid">

        <!-- Trumbull -->
        <div class="n9b-location-card">
          <div class="n9b-location-header">
            <div class="n9b-location-city">Trumbull</div>
            <div class="n9b-location-tag">Fairfield County, CT</div>
          </div>
          <div class="n9b-location-body">
            <div class="n9b-location-info">
              <div class="n9b-location-row">
                <span class="n9b-location-icon">📍</span>
                <div class="n9b-location-text">
                  <strong>Address</strong>
                  <a href="https://maps.google.com/?q=4244+Madison+Ave,+Trumbull,+CT+06611" target="_blank" rel="noopener">
                    4244 Madison Ave<br>Trumbull, CT 06611
                  </a>
                </div>
              </div>
              <div class="n9b-location-row">
                <span class="n9b-location-icon">📞</span>
                <div class="n9b-location-text">
                  <strong>Phone</strong>
                  <a href="tel:+12032611171">(203) 261-1171</a>
                </div>
              </div>
              <div class="n9b-location-row">
                <span class="n9b-location-icon">🕐</span>
                <div class="n9b-location-text">
                  <strong>Hours</strong>
                  <div class="n9b-location-hours">
                    Mon – Sat &nbsp;<span>10:00 AM – 9:00 PM</span><br>
                    Sunday &nbsp;<span>10:00 AM – 5:00 PM</span>
                  </div>
                </div>
              </div>
            </div>
            <a href="https://maps.google.com/?q=4244+Madison+Ave,+Trumbull,+CT+06611"
               target="_blank" rel="noopener" class="n9b-map-btn">
              📍 Get Directions
            </a>
          </div>
        </div>

        <!-- Westport -->
        <div class="n9b-location-card">
          <div class="n9b-location-header">
            <div class="n9b-location-city">Westport</div>
            <div class="n9b-location-tag">Fairfield County, CT</div>
          </div>
          <div class="n9b-location-body">
            <div class="n9b-location-info">
              <div class="n9b-location-row">
                <span class="n9b-location-icon">📍</span>
                <div class="n9b-location-text">
                  <strong>Address</strong>
                  <a href="https://maps.google.com/?q=9+Bridge+Square,+Westport,+CT+06880" target="_blank" rel="noopener">
                    9 Bridge Square<br>Westport, CT 06880
                  </a>
                </div>
              </div>
              <div class="n9b-location-row">
                <span class="n9b-location-icon">📞</span>
                <div class="n9b-location-text">
                  <strong>Phone</strong>
                  <a href="tel:+12032276672">(203) 227-6672</a>
                </div>
              </div>
              <div class="n9b-location-row">
                <span class="n9b-location-icon">🕐</span>
                <div class="n9b-location-text">
                  <strong>Hours</strong>
                  <div class="n9b-location-hours">
                    Mon – Sat &nbsp;<span>10:00 AM – 9:00 PM</span><br>
                    Sunday &nbsp;<span>10:00 AM – 5:00 PM</span>
                  </div>
                </div>
              </div>
            </div>
            <a href="https://maps.google.com/?q=9+Bridge+Square,+Westport,+CT+06880"
               target="_blank" rel="noopener" class="n9b-map-btn">
              📍 Get Directions
            </a>
          </div>
        </div>

        <!-- Norwalk -->
        <div class="n9b-location-card">
          <div class="n9b-location-header">
            <div class="n9b-location-city">Norwalk</div>
            <div class="n9b-location-tag">Fairfield County, CT</div>
          </div>
          <div class="n9b-location-body">
            <div class="n9b-location-info">
              <div class="n9b-location-row">
                <span class="n9b-location-icon">📍</span>
                <div class="n9b-location-text">
                  <strong>Address</strong>
                  <a href="https://maps.google.com/?q=209+Liberty+Square,+Norwalk,+CT+06855" target="_blank" rel="noopener">
                    209 Liberty Square<br>Norwalk, CT 06855
                  </a>
                </div>
              </div>
              <div class="n9b-location-row">
                <span class="n9b-location-icon">📞</span>
                <div class="n9b-location-text">
                  <strong>Phone</strong>
                  <a href="tel:+12038999937">(203) 899-9937</a>
                </div>
              </div>
              <div class="n9b-location-row">
                <span class="n9b-location-icon">🕐</span>
                <div class="n9b-location-text">
                  <strong>Hours</strong>
                  <div class="n9b-location-hours">
                    Mon – Sat &nbsp;<span>10:00 AM – 9:00 PM</span><br>
                    Sunday &nbsp;<span>10:00 AM – 5:00 PM</span>
                  </div>
                </div>
              </div>
            </div>
            <a href="https://maps.google.com/?q=209+Liberty+Square,+Norwalk,+CT+06855"
               target="_blank" rel="noopener" class="n9b-map-btn">
              📍 Get Directions
            </a>
          </div>
        </div>

      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ── Hours Banner ──────────────────────────────────────────────────────────────
st.markdown(
    """
    <section class="n9b-hours-banner" id="hours">
      <h2>Store Hours</h2>
      <p>All three locations keep the same convenient schedule</p>
      <table class="n9b-hours-table">
        <tbody>
          <tr><td>Monday</td><td>10:00 AM – 9:00 PM</td></tr>
          <tr><td>Tuesday</td><td>10:00 AM – 9:00 PM</td></tr>
          <tr><td>Wednesday</td><td>10:00 AM – 9:00 PM</td></tr>
          <tr><td>Thursday</td><td>10:00 AM – 9:00 PM</td></tr>
          <tr><td>Friday</td><td>10:00 AM – 9:00 PM</td></tr>
          <tr><td>Saturday</td><td>10:00 AM – 9:00 PM</td></tr>
          <tr><td>Sunday</td><td>10:00 AM – 5:00 PM</td></tr>
        </tbody>
      </table>
    </section>
    """,
    unsafe_allow_html=True,
)

# ── Photos / Gallery ─────────────────────────────────────────────────────────
st.markdown(
    """
    <section class="n9b-section n9b-gallery" id="photos">
      <div class="n9b-section-header">
        <span class="n9b-section-label">Inside Our Stores</span>
        <h2 class="n9b-section-title">Photo Gallery</h2>
        <p class="n9b-section-desc">
          Take a peek inside our Fairfield County locations—browse our curated
          selection of craft beers, wines, and spirits.
        </p>
      </div>
      <div class="n9b-gallery-cta">
        <div class="n9b-gallery-icon" aria-hidden="true">📷</div>
        <a href="https://share.google/wlVKOBrsN7oLDEADn"
           target="_blank"
           rel="noopener noreferrer"
           class="n9b-gallery-btn">
          View All Photos on Google Photos
        </a>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ── Social / Facebook ─────────────────────────────────────────────────────────
st.markdown(
    """
    <section class="n9b-section n9b-section-alt" id="social">
      <div class="n9b-section-header">
        <span class="n9b-section-label">Stay Connected</span>
        <h2 class="n9b-section-title">Follow Us on Facebook</h2>
        <p class="n9b-section-desc">
          Stay up to date on new arrivals, in-store tastings, special events, and
          promotions at all three of our Fairfield County locations.
        </p>
      </div>
      <div class="n9b-social-links">
        <a href="https://www.facebook.com/p/Ninety9Bottles-100057827252531/"
           target="_blank" rel="noopener" class="n9b-social-fb">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M24 12.073C24 5.405 18.627 0 12 0S0 5.405 0 12.073C0 18.1 4.388 23.094 10.125 24v-8.437H7.078v-3.49h3.047V9.41c0-3.025 1.792-4.697 4.533-4.697 1.312 0 2.686.236 2.686.236v2.97h-1.513c-1.491 0-1.956.93-1.956 1.886v2.267h3.328l-.532 3.49h-2.796V24C19.612 23.094 24 18.1 24 12.073z"/>
          </svg>
          Ninety 9 Bottles on Facebook
        </a>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <footer class="n9b-footer">
      <div class="n9b-footer-logo">99</div>
      <div class="n9b-footer-tagline">Ninety 9 Bottles · Fairfield County, CT</div>
      <div class="n9b-footer-locs">
        <div>
          <strong>Trumbull</strong>
          4244 Madison Ave, Trumbull, CT 06611<br>
          <a href="tel:+12032611171">(203) 261-1171</a>
        </div>
        <div>
          <strong>Westport</strong>
          9 Bridge Square, Westport, CT 06880<br>
          <a href="tel:+12032276672">(203) 227-6672</a>
        </div>
        <div>
          <strong>Norwalk</strong>
          209 Liberty Square, Norwalk, CT 06855<br>
          <a href="tel:+12038999937">(203) 899-9937</a>
        </div>
      </div>
      <hr class="n9b-footer-divider" />
      <p class="n9b-footer-copy">
        &copy; 2026 Ninety 9 Bottles. All rights reserved.
        &nbsp;&middot;&nbsp; Please drink responsibly. Must be 21+ to purchase alcohol.
      </p>
    </footer>
    """,
    unsafe_allow_html=True,
)

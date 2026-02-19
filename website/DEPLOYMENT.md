# Deployment Guide: Combine Harvester Website

Complete step-by-step guide to deploy the Combine Harvester website to GitHub Pages with Netlify CMS.

## Prerequisites

- GitHub account
- Git installed locally
- Basic command line knowledge (optional, can use GitHub web interface)

## Step 1: Enable GitHub Pages

1. **Go to repository settings**:
   - Navigate to https://github.com/n2fabian/manager
   - Click "Settings" tab
   - Click "Pages" in left sidebar

2. **Configure source**:
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/website` (or `/` if website is at root)
   - Click "Save"

3. **Wait for deployment**:
   - GitHub Actions will build the site
   - Check "Actions" tab for progress
   - Site will be live at: `https://n2fabian.github.io/manager/website/`

## Step 2: Configure Custom Domain (Optional)

### Purchase Domain

Recommended registrars:
- **Namecheap**: ~$12/year for .com
- **Google Domains**: ~$12/year
- **Porkbun**: ~$10/year

Suggested domains:
- `combineharvester.band` (~$30/year)
- `combineharvester.com` (~$12/year)
- `combineharvester.rocks` (~$15/year)

### Configure DNS

1. **Add DNS records** at your registrar:
   ```
   Type: CNAME
   Name: www
   Value: n2fabian.github.io
   ```

   ```
   Type: A (add all 4)
   Name: @
   Value: 185.199.108.153
   Value: 185.199.109.153
   Value: 185.199.110.153
   Value: 185.199.111.153
   ```

2. **Update GitHub Pages settings**:
   - Go to repository Settings → Pages
   - Custom domain: `combineharvester.band` (or your domain)
   - Check "Enforce HTTPS" (wait 24 hours for SSL cert)

3. **Update `_config.yml`**:
   ```yaml
   url: "https://combineharvester.band"
   baseurl: ""
   ```

### Verification

- Wait 24-48 hours for DNS propagation
- Visit your custom domain
- Verify HTTPS is working (🔒 in browser)

## Step 3: Set Up Netlify CMS

Netlify CMS allows non-technical users to edit content via a web interface.

### Create Netlify Account

1. Go to https://www.netlify.com/
2. Sign up with GitHub account (free tier)
3. No need to deploy site to Netlify (using GitHub Pages)

### Enable Netlify Identity

1. **Create new site** in Netlify:
   - Click "Add new site"
   - Choose "Import an existing project"
   - Connect to GitHub
   - Select `n2fabian/manager` repository
   - Build settings:
     - Base directory: `website`
     - Build command: `jekyll build`
     - Publish directory: `_site`
   - Click "Deploy site"

2. **Enable Identity service**:
   - Go to site settings
   - Click "Identity" in sidebar
   - Click "Enable Identity"

3. **Configure registration**:
   - Settings → Identity → Registration
   - Set to "Invite only" (recommended)
   - Save

4. **Enable Git Gateway**:
   - Settings → Identity → Services
   - Enable "Git Gateway"
   - This allows CMS to commit changes to GitHub

### Invite Users

1. **Invite band members**:
   - Identity tab → "Invite users"
   - Enter email addresses
   - They'll receive invite link

2. **Users set password**:
   - Click link in email
   - Set password
   - Can now access CMS

### Access CMS

- URL: `https://combineharvester.band/admin/` (or GitHub Pages URL + `/admin/`)
- Login with Netlify Identity credentials
- Edit content, add shows, upload images
- Changes are committed to GitHub automatically

## Step 4: Add Initial Content

### Via Git

```bash
cd website
# Edit files
git add .
git commit -m "Add initial content"
git push origin main
```

### Via Netlify CMS

1. Go to `/admin/`
2. Add shows to "Shows" collection
3. Upload band photos to "Media"
4. Update bio text
5. Click "Publish" to save

### Content to Add

- **Home page** (`index.html`):
  - Hero image
  - Short bio
  - Latest news

- **Music page** (`music.html`):
  - Spotify embed (get from Spotify artist page)
  - Streaming links
  - Release history

- **Shows** (via CMS):
  - Upcoming show dates
  - Venue information
  - Ticket links

- **Media** (`media.html`):
  - Band photos
  - Live videos
  - Press photos

## Step 5: Configure Analytics (Optional)

### Google Analytics

1. **Create GA4 property**:
   - Go to https://analytics.google.com/
   - Create new property
   - Get Measurement ID (e.g., `G-XXXXXXXXXX`)

2. **Add to `_config.yml`**:
   ```yaml
   google_analytics: G-XXXXXXXXXX
   ```

3. **Add tracking code** to `_layouts/default.html` (if not using plugin):
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id={{ site.google_analytics }}"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', '{{ site.google_analytics }}');
   </script>
   ```

### Plausible Analytics (Privacy-Friendly Alternative)

1. Sign up at https://plausible.io/
2. Add site domain
3. Add tracking script to `_layouts/default.html`:
   ```html
   <script defer data-domain="combineharvester.band" src="https://plausible.io/js/script.js"></script>
   ```

## Step 6: Test Everything

### Checklist

- [ ] Site loads at GitHub Pages URL
- [ ] All pages are accessible (home, music, shows, media, contact)
- [ ] Images load correctly
- [ ] Spotify embed plays music
- [ ] Contact form works
- [ ] Mobile responsive (test on phone)
- [ ] Netlify CMS login works
- [ ] CMS can create/edit content
- [ ] Changes appear on live site
- [ ] Custom domain works (if configured)
- [ ] HTTPS is enforced
- [ ] Analytics tracking works (if configured)

### Troubleshooting

**Site not building**:
- Check GitHub Actions for build errors
- Verify Jekyll syntax in files
- Check `_config.yml` for typos

**CMS not loading**:
- Verify Netlify Identity is enabled
- Check `admin/config.yml` configuration
- Ensure Git Gateway is enabled

**Custom domain not working**:
- Wait 24-48 hours for DNS propagation
- Verify DNS records are correct
- Check GitHub Pages settings

**Images not appearing**:
- Verify image paths are correct
- Check file extensions (case-sensitive)
- Ensure images are in `assets/images/`

## Step 7: Ongoing Maintenance

### Regular Tasks

**Weekly**:
- Add upcoming shows
- Update news/announcements
- Check analytics

**Monthly**:
- Review site performance
- Update band photos
- Check for broken links

**As Needed**:
- Add new releases
- Update bio
- Modify design/layout

### Backups

- GitHub repository serves as backup
- All changes are version controlled
- Can revert to any previous version

### Updates

**Security updates**:
```bash
cd website
bundle update
git add Gemfile.lock
git commit -m "Update dependencies"
git push
```

**Content updates**:
- Use Netlify CMS for non-technical updates
- Direct Git commits for technical changes

## Support Resources

- **Jekyll Documentation**: https://jekyllrb.com/docs/
- **GitHub Pages Guide**: https://docs.github.com/en/pages
- **Netlify CMS Docs**: https://www.netlifycms.org/docs/
- **Custom Domain Setup**: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

## Estimated Costs

- **GitHub Pages**: Free
- **Netlify CMS**: Free (basic tier)
- **Custom domain**: $10-30/year (optional)
- **Analytics**: Free (GA or Plausible free tier)

**Total**: $0-30/year

---

*Last Updated: 2026-02-19*

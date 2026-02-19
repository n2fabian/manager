# Combine Harvester - Band Website

Official website for **Combine Harvester**, a heavy metalcore band from North Rhine-Westphalia, Germany.

## About

This website is built with Jekyll and hosted on GitHub Pages, featuring:
- Clean, modern design optimized for music bands
- Mobile-responsive layout
- Non-technical content management via Netlify CMS
- Free hosting with HTTPS support
- Easy updates for show dates, news, and media

## Technology Stack

- **Static Site Generator**: Jekyll 4.x
- **Hosting**: GitHub Pages (free)
- **CMS**: Netlify CMS (for easy content updates)
- **CSS**: Custom styles with mobile-first design
- **JavaScript**: Minimal, progressive enhancement

## Local Development

### Prerequisites

- Ruby 2.7+ (for Jekyll)
- Bundler
- Git

### Setup

1. **Install dependencies**:
   ```bash
   cd website
   bundle install
   ```

2. **Run local server**:
   ```bash
   bundle exec jekyll serve
   ```

3. **View site**:
   Open http://localhost:4000 in your browser

### Making Changes

- **Content**: Edit markdown files or use Netlify CMS admin panel
- **Layout**: Modify files in `_layouts/` and `_includes/`
- **Styles**: Edit `assets/css/style.css`
- **Configuration**: Update `_config.yml`

## Deployment

See `DEPLOYMENT.md` for complete deployment instructions.

**Quick Deploy**:
1. Push changes to `main` branch
2. GitHub Pages automatically rebuilds
3. Site updates in 1-2 minutes

## Content Management

### For Non-Technical Users

1. Go to `https://your-site.com/admin/`
2. Log in with Netlify Identity
3. Add/edit shows, update bio, upload images
4. Click "Publish" to save changes

### For Technical Users

- Direct Git commit access
- Full HTML/CSS/JS editing
- Custom functionality via Jekyll plugins
- Advanced analytics and tracking

## Structure

```
website/
├── _config.yml           # Jekyll configuration
├── _layouts/             # Page layouts
├── _includes/            # Reusable components
├── _data/                # Data files (shows, social links)
├── _shows/               # Individual show pages
├── admin/                # Netlify CMS config
├── assets/               # CSS, JS, images
├── index.html            # Home page
├── music.html            # Music & releases
├── shows.html            # Show calendar
├── media.html            # Photos & videos
└── contact.html          # Contact & booking
```

## Features

- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Fast loading (<2s on 3G)
- ✅ SEO optimized
- ✅ Social media integration
- ✅ Spotify embed support
- ✅ Easy show date management
- ✅ Image gallery
- ✅ Contact form
- ✅ Google Analytics ready

## Customization

### Colors

Edit `assets/css/style.css`:
```css
:root {
  --primary-color: #e53935;      /* Red accent */
  --bg-dark: #1a1a1a;            /* Dark background */
  --text-light: #f5f5f5;         /* Light text */
}
```

### Logo

Replace `assets/images/logo.png` with your band logo

### Fonts

Edit in `_layouts/default.html` or link Google Fonts

## Support

- **Technical Issues**: Open an issue in GitHub repository
- **Content Questions**: Contact band manager
- **Jekyll Docs**: https://jekyllrb.com/docs/

## License

Website code: MIT License
Band content (images, music, text): © Combine Harvester, all rights reserved

---

*Last Updated: 2026-02-19*

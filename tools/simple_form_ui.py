# Simple Form UI for Band Manager
#
# This script provides a basic web-based form UI for collecting information in a structured, multi-step way.
# It uses Flask for the backend and WTForms for form handling. If not installed, please install Flask and WTForms.

from flask import Flask, render_template_string, request, redirect, url_for, session
from wtforms import Form, StringField, BooleanField, TextAreaField, validators, SubmitField, FieldList, FormField
from markupsafe import Markup
import os
import json


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'bandmanagersecret')


# --- FORMS ---
class BandInfoForm(Form):
    band_name = StringField('Band Name *', [validators.InputRequired()])
    band_name_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    members = TextAreaField('Band Members & Roles *', [validators.InputRequired()], render_kw={"placeholder": "One per line. Use Shift+Enter for new line."})
    members_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    bio_short = TextAreaField('Short Bio *', [validators.InputRequired()])
    bio_short_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    bio_long = TextAreaField('Long Bio (optional)')
    bio_long_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    music_links = TextAreaField('Music Links (Spotify, etc) *', [validators.InputRequired()], render_kw={"placeholder": "One per line. Use Shift+Enter for new line."})
    music_links_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    social_links = TextAreaField('Social Media Links (optional)', render_kw={"placeholder": "One per line. Use Shift+Enter for new line."})
    social_links_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    past_shows = TextAreaField('Past Shows (optional)', render_kw={"placeholder": "One per line. Use Shift+Enter for new line."})
    past_shows_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    merch = TextAreaField('Current Merch (optional)', render_kw={"placeholder": "One per line. Use Shift+Enter for new line."})
    merch_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    tech_reqs = TextAreaField('Special Tech Requirements (optional)', render_kw={"placeholder": "One per line. Use Shift+Enter for new line."})
    tech_reqs_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    submit = SubmitField('Save')
    cancel = SubmitField('Cancel')
    skip = SubmitField('Skip')

class ContactForm(Form):
    name = StringField('Your Name *', [validators.InputRequired()])
    name_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    email = StringField('Email *', [validators.InputRequired(), validators.Email()])
    email_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    phone = StringField('Phone (optional)')
    phone_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    other = StringField('Other Contact (optional)')
    other_note = TextAreaField('Note to Agent (optional)', render_kw={"placeholder": "Extra info for the agent only"})
    submit = SubmitField('Save')
    cancel = SubmitField('Cancel')
    skip = SubmitField('Skip')


# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def start():
    return redirect(url_for('band_info', band='nears-2-far'))

@app.route('/band-info/<band>', methods=['GET', 'POST'])
def band_info(band):
    form = BandInfoForm(request.form)
    if request.method == 'POST':
        if form.cancel.data:
            return render_template_string(MINIMAL_TEMPLATE, title='Cancelled', content='Operation cancelled.')
        if form.skip.data:
            session[f'band_{band}_info'] = 'skipped'
            return redirect(url_for('contact_info'))
        if form.validate():
            session[f'band_{band}_info'] = request.form.to_dict()
            # Save to file for agent access
            save_path = os.path.join(os.path.dirname(__file__), f'band_{band}_info.json')
            with open(save_path, 'w') as f:
                json.dump(request.form.to_dict(), f, indent=2)
            if band == 'nears-2-far':
                return redirect(url_for('band_info', band='combine-harvester'))
            else:
                return redirect(url_for('contact_info'))
    return render_template_string(MINIMAL_TEMPLATE, title=f"{band.replace('-', ' ').title()} Info", form=form)

@app.route('/contact-info', methods=['GET', 'POST'])
def contact_info():
    form = ContactForm(request.form)
    if request.method == 'POST':
        if form.cancel.data:
            return render_template_string(MINIMAL_TEMPLATE, title='Cancelled', content='Operation cancelled.')
        if form.skip.data:
            session['contact_info'] = 'skipped'
            return render_template_string(MINIMAL_TEMPLATE, title='Done', content='You can now continue in the system.')
        if form.validate():
            session['contact_info'] = request.form.to_dict()
            # Save to file for agent access
            save_path = os.path.join(os.path.dirname(__file__), 'contact_info.json')
            with open(save_path, 'w') as f:
                json.dump(request.form.to_dict(), f, indent=2)
            return render_template_string(MINIMAL_TEMPLATE, title='Done', content='You can now continue in the system.')
    return render_template_string(MINIMAL_TEMPLATE, title='Your Contact Info', form=form)


MINIMAL_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }}</title>
    <style>
        body { background: #181818; color: #f5f5f5; font-family: 'Inter', Arial, sans-serif; margin: 0; padding: 0; }
        .container { max-width: 520px; margin: 48px auto; background: #232323; border-radius: 12px; box-shadow: 0 2px 16px #0008; padding: 32px 28px; }
        h2, h1 { font-weight: 600; margin-bottom: 24px; letter-spacing: 0.01em; }
        form { display: flex; flex-direction: column; gap: 18px; }
        label { font-size: 1.05em; margin-bottom: 4px; color: #e0e0e0; }
        input, textarea { background: #181818; color: #f5f5f5; border: 1px solid #444; border-radius: 6px; padding: 10px; font-size: 1em; transition: border 0.2s; }
        input:focus, textarea:focus { border: 1.5px solid #7e57c2; outline: none; }
        textarea { min-height: 60px; resize: vertical; font-family: inherit; }
        .form-actions { display: flex; gap: 12px; margin-top: 10px; }
        button, input[type=submit] { background: #7e57c2; color: #fff; border: none; border-radius: 6px; padding: 10px 18px; font-size: 1em; cursor: pointer; transition: background 0.2s; }
        button:hover, input[type=submit]:hover { background: #9575cd; }
        .secondary { background: #444; color: #ccc; }
        .secondary:hover { background: #666; }
        .skip { background: #232323; color: #aaa; border: 1px solid #444; }
        .skip:hover { background: #333; color: #fff; }
        .content { margin-top: 24px; font-size: 1.1em; }
        .note-label { font-size: 0.98em; color: #b39ddb; margin-top: 2px; margin-bottom: 2px; }
        .note-field { background: #181818; color: #b39ddb; border: 1px dashed #7e57c2; }
    </style>
    <script>
        // Allow Shift+Enter for newlines in textarea, Enter to submit
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('textarea').forEach(function(el) {
                el.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter' && !e.shiftKey) {
                        // Prevent Enter from submitting if in textarea
                        e.stopPropagation();
                    }
                });
            });
        });
    </script>
</head>
<body>
    <div class="container">
        <h2>{{ title }}</h2>
        {% if form %}
        <form method="post">
            {% for field in form if field.type != 'CSRFToken' %}
                {% if 'note' in field.name %}
                    <div>
                        <span class="note-label">{{ field.label }}</span><br>
                        {{ field(rows=2, cols=36, class_="note-field") }}
                    </div>
                {% else %}
                    <div>
                        {{ field.label }}<br>
                        {{ field(size=36) if field.type == 'StringField' else field(rows=3, cols=36) }}
                        {% if field.errors %}
                            <div style="color:#ff5252; font-size:0.95em;">{{ field.errors[0] }}</div>
                        {% endif %}
                    </div>
                {% endif %}
            {% endfor %}
            <div class="form-actions">
                {{ form.submit(class_="") }}
                {{ form.cancel(class_="secondary") }}
                {{ form.skip(class_="skip") }}
            </div>
        </form>
        {% elif content %}
            <div class="content">{{ content|safe }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)

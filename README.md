# AGGC Streamlit Website

A Streamlit-ready business website for **Abraham Gizaw General Construction (AGGC)**.

## Features

- Modern construction-company landing page
- Responsive desktop/mobile layout
- English, Amharic (አማርኛ), and Afaan Oromoo language selector
- Service sections for roads, bridges/culverts, irrigation, WASH, electrical installation, and buildings
- About, values, delivery process, and quotation-request sections
- Uses the supplied AGGC artwork and service imagery
- No invented phone number, email, address, project count, or client list

## 1. Add verified company contact details

Open `app.py` and edit the `COMPANY` dictionary near the top:

```python
COMPANY = {
    "name": "ABRAHAM GIZAW GENERAL CONSTRUCTION",
    "short_name": "AGGC",
    "email": "",
    "phone": "",
    "whatsapp": "",
    "address": "",
    "facebook": "",
    "linkedin": "",
}
```

Only enter verified details. WhatsApp should use international digits without `+`, spaces, or dashes.

## 2. Test locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 3. Publish on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload the contents of this folder to the repository root.
3. Go to Streamlit Community Cloud.
4. Choose **Create app / New app**.
5. Select your GitHub repository and branch.
6. Set the main file path to `app.py`.
7. Click **Deploy**.

No secrets are required for the current version.

## Recommended before public launch

- Replace illustrative service imagery with verified photographs from completed AGGC projects.
- Add verified phone, email, office address, WhatsApp, and social links.
- Add a project portfolio once project names, locations, clients, dates, and photographs are confirmed for publication.
- Have the Amharic and Afaan Oromoo text reviewed by a native professional translator before formal tender/business use.
- If you want enquiry forms to be emailed automatically, connect a verified mailbox or form backend rather than relying on local Streamlit session state.

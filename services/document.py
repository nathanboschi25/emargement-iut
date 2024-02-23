import base64
from datetime import datetime
import os

import pdfkit
from jinja2 import Template


def render_template_to_html_as_str(template_file, **kwargs):
    with (open(template_file, 'rb')) as f:
        return Template(f.read().decode('utf-8')).render(**kwargs)


def get_image_base64(dept_name):
    # search for the image in the images folder
    imagepath = os.path.join('assets', 'logos-iut', dept_name + '.png')
    with open(imagepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')


def generate_pdf(program_args, events, students):
    html = render_template_to_html_as_str(program_args.template, dep_logo=get_image_base64(os.getenv('DEPT')), len=len,
                                          classe=os.getenv('CLASS'), day=program_args.day.strftime('%d/%m/%Y'),
                                          students=students, cours=events)
    config = pdfkit.configuration(wkhtmltopdf=os.getenv('WKHTMLTOPDF_PATH'))
    today = datetime.now().strftime("%d/%m/%Y")

    pdfkit.from_string(html, program_args.output,
                       options={"margin-left": "5mm", "margin-right": "5mm", "margin-bottom": "5mm",
                                "margin-top": "5mm", "encoding": "utf-8",
                                "footer-center": "Fiche générée le {} avec emargement-iut © Nathan BOSCHI\nVoir https://github.com/nathanboschi25/emargement-iut\n".format(today),
                                "footer-font-size": "8"}, configuration=config)

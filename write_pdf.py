import asyncio
import os
from pyppeteer import launch

async def generate_pdf_from_html(html_file_path, pdf_file_path):
    #print(f"HTML File Path: {html_file_path}")

    # Check if the HTML file exists
    if not os.path.exists(html_file_path):
        print("Error: The HTML file does not exist.")
        return

    #print("Launching the browser...")

    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto('file://' + html_file_path)
        await page.pdf({'path': pdf_file_path, 'format': 'A4', 'printBackground': True})
    except Exception as e:
        raise Exception(e)
    finally:
        await browser.close()

#Write cv to pdf
def write_cv(html_cv_path, pdf_cv_path):
    asyncio.get_event_loop().run_until_complete(generate_pdf_from_html(html_cv_path, pdf_cv_path))
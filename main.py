import populate_cv
import write_pdf
import os
import shutil

def main():
    template_path = os.path.abspath('./templates/cv/')
    output_html_path = os.path.abspath('./output/html/')

    # Copy the template directory path to the output path
    shutil.copytree(template_path, output_html_path, symlinks=False, dirs_exist_ok=True)

    html_cv_path = os.path.abspath(output_html_path + '/index.html')
    cv_data_path = os.path.abspath('./data/cv_data.json')
    
    # Populate the output HTML CV
    populate_cv.populate_html_template(html_cv_path, cv_data_path)
    print("INFO: CV HTML populated and saved successfully! In directory: "  + html_cv_path)
   
    # Create PDF in pdf_cv_path
    try:
        pdf_cv_path = os.path.abspath('./output/pdf/cv.pdf')
        write_pdf.write_cv(html_cv_path, pdf_cv_path)
        print(f"INFO: CV saved at: {pdf_cv_path}")
    except RuntimeError as e:
        print(f"ERROR: generating the PDF: {str(e)}")


if __name__ == "__main__":
    main()
import populate_cv
import write_pdf
import os
import shutil

def mkdir(fname):
    try:
        os.mkdir(fname)
    except:
        pass

def main():
    output_html_path = os.path.abspath('./output/html')
    output_pdf_path = os.path.abspath('./output/pdf')
    template_path = os.path.abspath('./templates/cv')
    html_cv_path = os.path.abspath(output_html_path + '/index.html')
    pdf_cv_path = os.path.abspath(output_pdf_path + '/cv.pdf')
    cv_data_path = os.path.abspath('./data/cv_data.json')

    # Create output dir
    mkdir(output_html_path)
    mkdir(output_pdf_path)

    # Copy the template directory path to the output path
    shutil.copytree(template_path, output_html_path, dirs_exist_ok=True)
    
    # Populate the output HTML CV
    populate_cv.populate_html_template(html_cv_path, cv_data_path)
    print("INFO: CV HTML populated and saved successfully! In directory: "  + html_cv_path)
   
    # Create PDF in pdf_cv_path
    try:
        write_pdf.write_cv(html_cv_path, pdf_cv_path)
        print(f"INFO: CV saved at: {pdf_cv_path}")
    except RuntimeError as e:
        print(f"ERROR: generating the PDF: {str(e)}")


if __name__ == "__main__":
    main()
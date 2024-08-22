        behave -f json -o Reports/my_json_out.json Features/Login.feature

        python custom_report_generator/report_generator.py --input_json_file Reports/my_json_out.json --output_html_file report1.html

        behave -f json -o Reports/my_json_out.json Features/Login.feature --no-capture --tags=LoginPage

        behave -f json -o Reports/my_json_out.json Features/Login.feature --no-capture --tags=LoginPage,CreateShipment
        python Features/runner.py Features/1Login.feature Features/2CELogin.feature

        ---

        For report--> behave -f allure_behave.formatter:AllureFormatter -o Reports Features/Login.feature
        For Report Generation-->allure serve Reports/

        behave -f json -o Reports/my_json_out.json Features/Login.feature --no-capture --tags=LoginPage

        ---

        For Execution-->behave Features\Login.feature
        For allur report--> behave -f allure_behave.formatter:AllureFormatter -o Reports Features/Login.feature
        For Report Generation-->allure serve Reports/
        for Report HTML-->behave -v -s --html=report.html Features/Login.feature
        behave --junit --junit-directory my_reports
        behave -f json -o my_json_out.json
        python custom_report_generator/report_generator.py --input_json_file my_json_out.json --output_html_file report1.html

        python custom_report_generator/report_generator.py --input_json_file Reports/my_json_out.json --output_html_file report1.html

# -*- coding: utf-8 -*-
"""

"""

html_code = """
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Template</title>
    <style type="text/css">
        body {
            Margin: 0;
            padding: 0;
            background-color: #f6f9fc;
        }

        table {
            border-spacing: 0;
        }

        td {
            padding: 0;
        }

        img {
            border: 0;
        }

        .wrapper {
            width: 100%;
            table-layout: fixed;
            background-color: #f6f9fc;
            padding-bottom: 40px;
        }

        .webkit {
            max-width: 600px;
            background-color: #ffffff;
        }

        .outer {
            margin: 0 auto;
            width: 100%;
            max-width: 600px;
            border-spacing: 0;
            font-family: sans-serif;
            color: #4a4a4a;
        }

        .three-columns {
            text-align: center;
            font-size: 0;
            padding-top: 40px;
            padding-bottom: 30px;
        }

        .three-columns .column {
            width: 100%;
            max-width: 200px;
            display: inline-block;
            vertical-align: top;
        }

        .padding {
            padding: 15px;
        }

        .three-columns .content {
            font-size: 15px;
            line-height: 20px;
        }

        a {
            text-decoration: none;
            color: #388CDA;
            font-size: 16px;
        }

        @media screen and (max-width: 600px) {
            img.third-img-last {
                width: 200px !important;
                max-width: 200px !important;
            }

            .padding {
                padding-right: 0 !important;
                padding-left: 0 !important;
            }
        }

        @media screen and (max-width: 400px) {
            img.third-img {
                width: 200px !important;
                max-width: 200px !important;
            }
        }
    </style>
</head>

<body>

    <center class="wrapper">
        <div class="webkit">

            <table class="outer" align="center" border="0">

                <div class="grid">
                   
					<p>Hello *|FNAME|* *|LNAME|*,</p>
                    <p>queremos compartir un pequeño video que hemos hecho para ti:</p>
        			<img width="320" height="176">
   					   <!-- fallback 1 -->
     					<a href=*|URLVIDEO|* ><img height="176" 
       					 src="https://assetsjrtec.s3.us-east-2.amazonaws.com/Dise%C3%B1o+sin+t%C3%ADtulo+(1).png" width="320" /></a>
					</img>
                </div>
			


            </table>

        </div>
    </center>

</body>

</html>
			
   		
"""





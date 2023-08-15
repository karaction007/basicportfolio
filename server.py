from flask import Flask,render_template,redirect,url_for,request
import csv
app=Flask(__name__)

# print(app)

@app.route('/')
def homepage():
    return render_template('./index.html')

@app.route('/index.html')
def to_homepage():
    return redirect('/')

@app.route('/<string:html_page>')
def send_page(html_page=None):
    return render_template(html_page)

def add_record_to_file(data=None):
    if data is None:
        return 1
    else:
        try:
            with open("db.txt","a") as db:
                db.write(f"\n{data['email']},{data['subject']},{data['message']}")
        except:
            return 1    
        else:
            return 0

def add_record_to_csv(data=None):
    if data is None:
        return 1
    else:
        try:
            with open("db.csv",newline='',mode="a") as db:
                csv_writer=csv.writer(db,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([data['email'],data['subject'],data['message']])
        except:
            return 1    
        else:
            return 0

@app.route('/submit_info', methods=['POST', 'GET'])
def submit_info():
    if request.method == 'POST':
        data=request.form.to_dict()
        add_record_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Error."
    

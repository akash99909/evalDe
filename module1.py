from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def first():
    return render_template('homw.html')

@app.route('/form')
def form():
    return render_template('HTMLPage1.html')
@app.route('/form',methods=['POST', 'GET'])
def getData():
    s1 =  request.form.getlist('sen1[]')
    s2 =  request.form.getlist('sen2[]')
    s3 =  request.form.getlist('sen3[]')
    s4 =  request.form.getlist('sen4[]')
    s5 =  request.form.getlist('sen5[]')
    s6 =  request.form.getlist('sen6[]')
    s7 =  request.form.getlist('sen7[]')
    s8 =  request.form.getlist('sen8[]')
    s9 =  request.form.getlist('sen9[]')
    s10=  request.form.getlist('sen10[]')
    s11=  request.form.getlist('sen11[]')
    s12=  request.form.getlist('sen12[]')

    conn = mysql.connector.connect(user='padfoot', password='password',host='localhost',database='de_accelerator',auth_plugin='mysql_native_password')
    if conn:
        print ("Connected Successfully") 
    else:
        print ("Connection Not Established")
    cursor = conn.cursor()
    count = 0
    for i in range(len(s1)):
        sql = "INSERT INTO de_accelerator (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (s1[i],s2[i],s3[i],s4[i],s5[i],s6[i],s7[i],s8[i],s9[i],s10[i],s11[i],s12[i])
        cursor.execute(sql,val)
        conn.commit()
        count += 1

    sql2 = "SELECT s11 from de_accelerator order by f1 desc"
    cursor.execute(sql2)
    rows = cursor.fetchmany(count)
    sum = 0
    if rows:
        for row in rows:
            if row[0] == "":
                continue
            sum = sum + int(row[0])
    print(sum)

    return render_template('calculation.html',sum = sum,per = 0)

@app.route('/form1',methods=['POST', 'GET'])
def calculate():
    data = request.form['per']
    data1 =  request.form['sum']
    print(data)
    value = (int(data) * int(data1))/100
    return render_template('calculation.html',sum = data1,per = value)

app.run(host='localhost', port=5000, debug = True)

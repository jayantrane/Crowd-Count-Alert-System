from flask import Flask, render_template, Response,request
from camera import VideoCamera, VideoCamera2
import math
app = Flask(__name__)
mcnt = -1
mcnt2 = -1
side1 ='left'
side2 = 'right'
etcount = 0;
@app.route('/')
def index():

    return render_template('index.html')

def gen(camera):
    count =0
    while True:
        frame,etcount,sid1 = camera.get_frame(count)
        #     # save frame as JPEG filea
        #atime.sleep(0.1)
        
        count += 1
        global mcnt
        print("count 1 = " , mcnt)
        
        global side1
        if(etcount!=0):
            mcnt = etcount
            side1 = sid1
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen2(camera):
    count =0
    while True:
        frame,etcount,sid2 = camera.get_frame(count)
        #     # save frame as JPEG filea
        #atime.sleep(0.1)
        
        count += 1
        global mcnt2
        global side2
        print("count2 = ", mcnt2)
       
        if(etcount!=0):
            mcnt2 = etcount
            side2 = sid2
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
                
@app.route('/video_feed')
def video_feed():
     #os.system('python cameratest.py')
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
     #os.system('python cameratest.py')
    return Response(gen2(VideoCamera2()),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/answer')
def answer():
    return render_template("test12.html",text=str(etcount))

@app.route('/answer2')
def answer2():
    return render_template("test122.html",text=str(etcount))

@app.route('/suggestions')
def suggestions():
    text = request.args.get('jsdata')

    suggestions_list = []

    
    global mcnt
    global side1
    
    str1 = str(abs(math.ceil(mcnt)))
    
    suggestions_list.append(str1)
    suggestions_list.append(side1)
    

    return render_template('suggestions.html', suggestions=suggestions_list)

@app.route('/suggestions2')
def suggestions2():
    text = request.args.get('jsdata')

    suggestions_list = []

    global mcnt2
    global side2
    
    str1 = str(abs(math.ceil(mcnt2)))
    
    suggestions_list.append(str1)
    suggestions_list.append(side2)
    

    return render_template('suggestions.html', suggestions=suggestions_list)
@app.route('/s1')
def s1():
    text = request.args.get('jsdata')

    suggestions_list = []

    
    global side1
    if side1 == "left" :
        str2 = "0"
    else:
        str2 = "1"

    suggestions_list.append(str2)

    return render_template('suggestions.html', suggestions=suggestions_list)
@app.route('/s2')
def s2():
    text = request.args.get('jsdata')

    suggestions_list = []

    
    global side2
    if side2 == "left" :
        str2 = "0"
    else:
        str2 = "1"
    suggestions_list.append(str2)

    return render_template('suggestions.html', suggestions=suggestions_list)


if __name__ == '__main__':

    app.run(debug=True)

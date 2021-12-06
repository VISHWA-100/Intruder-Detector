import smtplib
import imghdr
from email.message import EmailMessage



def sendEmail(path):
    #Sender_Email = "-------------------"
    #Reciever_Email = "----------------"
    #Password = "-----------"

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Clinics Project successfull...... Mail from the project!!!!!!!!!!!!!" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content("Here is the image of detected intruder.... ") 

    with open(path, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)

def callfn(j):

        i=5;
        if i > 0:
            
            path = "C:\\Users\\K.VISHWA\\Documents\\clinics\\sample"+str(j)+".jpg"

            sendEmail(path)


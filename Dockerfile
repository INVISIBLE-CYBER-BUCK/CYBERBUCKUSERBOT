FROM INVISIBLE-CYBER-BUCK/CYBERBUCKBOT:slim-buster

#clonning repo 

RUN git clone https://github.com/INVISIBLE-CYBER-BUCK/CYBERBUCKUSERBOT.git /root/Cyberbot

#working directory 
WORKDIR /root/Cyberbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Cyberbot/bin:$PATH"

CMD ["python3","-m","Cyberbot"]

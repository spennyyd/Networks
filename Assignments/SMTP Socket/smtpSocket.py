from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('mail.letu.edu', 25)
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('mail.letu.edu', 25))
# Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCmd = 'Mail FROM: <spencerdavis@letu.edu>\r\n'
clientSocket.send(mailFromCmd)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
    print '250 reply not received from server.'
# Fill in end


# Send RCPT TO command and print server reponse.
# FIll in start
rcptToCommand = 'RCPT TO: <spencerdavis@letu.edu>\r\n'
clientSocket.send(rcptToCommand)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
    print '250 reply not received from server.'
# Fill in end


# Send DATA command and print server resonse.
# Fill in start
clientSocket.send('DATA\r\n')
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '354':
    print '354 reply not received from server'
# Fill in end


# Send message data.
# Fill in start
clientSocket.send('SUBJECT: Greeting To you!\r\n')
clientSocket.send('test again')
clientSocket.send(msg)
# Fill in end


# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '250':
    print '250 reply not received from server.'
# Fill in end


# Send QUIT command and get server response.
# Fill in start
quitMsg = 'QUIT\r\n'
clientSocket.send(quitMsg)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '221':
    print '221 reply not received from server.'
clientSocket.close()
# Fill in end
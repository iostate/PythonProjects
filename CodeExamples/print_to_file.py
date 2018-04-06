# Create a session information file and add the Session ID and URL to the
# file.

session_file = open("sessioninformation.txt", "w")
session_file.write("http://127.0.0.1:52026\n")
session_file.write('dffd57e5-d211-8540-add9-b98991d3a05f\n')
session_file.close()

# read_sess_file = open('sessioninformation.txt', 'r')
with open('sessioninformation.txt') as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print line.strip()
        line = fp.readline()
        cnt += 1


# Read the file line by line

![Deploy badge](https://github.com/Daniel-Tol/assignment_CD/actions/workflows/main.yml/badge.svg)

---

### **Three components of my solution:**

I used SSH to connect from the Github repository to the IP Address of the droplet.

**SSH:** SSH is a network communication protocol that makes it possible for two computers to communicate with one another.

**Github repository:** A repository on Github containing all of the project's files and each file's revision history.

**IP Address:** An IP address is a unique address that identifies a device on the internet or a local network.

---

### **Three problems that I encountered along the way and how I solved them:**

**1:** Using appleboy to deploy with SSH, I had trouble connecting. First I thought it to be an issue with Github secrets, it turned out to be a misunderstanding of what the host address was. Because of a tutorial I watched I thought it was the (numeric) address after the 'root@' in the droplet console. After a while I instead tried out the IP address of the droplet and it connected.

**2:** While messing around with secets, I wanted to rule out if the issue was with the secrets. So I used the log-in credentials in the repository itself. After figuring out the first problem, I wanted to delete the log-in credentials from the github repository commits. This wasn't possible, so I deleted the entire repository on Github Desktop. I didn't realise this would also delete the entire folder on my computer. Since it wasn't much code, I put everything back together quite fast, but when I was trying to connect I got an error telling me the public key was already in use. It turned out the repository wasn't completely deleted on Github, so I didn't need to write everything again. I restored the deleted repository to take out the key, and put it in the current repository.

**3:** After succesfully connecting and deploying, I wanted to see the 'main.py' live in action. To do this, I refered back to the 'Deployment' exercise, and created a 'assignment_CD.service' file for the folder of the assignment. After starting the service and checking up on it, it said the address was already in use. I disabled the previous 'farm' service and now I could see the deployed 'main.py'.

---

### **Anything of note I want to share during the process of this assignment:**

First I used the example code of the 'GitHub Actions and Python' segment in the '@app.route'. This wouldn't display anything. Since the complexity of the Flask Application wasn't the point of the assignment, I refered back to the even simpler code in the 'Deployment' exercise. I also added some extra farm animals to test with!

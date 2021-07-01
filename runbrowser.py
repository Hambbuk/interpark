import os
import pyautogui
from time import sleep


class Browser:
    def init(self, folder='C:/Program Files/Google/Chrome/Application', port='9222', temp='C:/Chrome_debug_temp'):
        self.folder = folder
        self.port = port
        self.temp = temp
        self.chrome_start = 'start chrome.exe --remote-debugging-port='+self.port+' --user-data-dir="'+self.temp+'/'+self.port+'"'
        self.chrome_close = 'FOR /F "tokens=5 delims= " %%I IN ('netstat -ano ^| find '":'+port\
                            +'" ^| find "CLOSE_WAIT"') DO (taskkill /F /PID %%I)'

    def run(self):
        if self.is_run() is False:
            os.chdir(self.folder)
            os.system(self.chrome_start)
            print('Chrome is going to run')
        else:
            yn = pyautogui.confirm('Restart Chrome?')
            if yn == "OK":
                print('Restart Chrome')
                self.close()
                os.chdir(self.folder)
                os.system(self.chrome_start)
            else:
                print('Canceled')

    def is_run(self):
        output = self.netstat()
        if output.find('127.0.0.1:'+self.port) == -1:
            return False
        else:
            return True

    def netstat(self):
        output = os.popen('netstat -ano | findstr '+self.port).read()
        return output

    def close(self):
        os.system(self.chrome_close)
        return


if name == "main":
    chrome = Browser(port='9222')
    chrome.run()
    sleep(1)
    print(chrome.netstat())
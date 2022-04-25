import time
import csv
class KebukeBranch:
    def __init__(self,driver):
        self.driver = driver
        self.config = self.driver.config

    def kebukeBranch(self):

        result=[]
        locations=['基隆門市','台北門市','新北門市','桃園門市','新竹門市','苗栗門市','台中門市','彰化門市','南投門市',
                  '雲林門市','嘉義門市','台南門市','高雄門市','屏東門市','宜蘭門市','花蓮門市','台東門市','澎湖門市','金門門市']
        default = '台北門市'
        for i in locations:
            self.driver.clickItem("//div[@class ='form-dropdown__select-now' and contains(text(),'"+default+"')]")
            self.driver.clickItem("//div[@class= 'form-dropdown__option' and contains(text(),'"+i+"')]")
            default = i
            result += [i]
            self.driver.waitUntilAppear( "//div[@class='archive-store__main']")
            result +=self.driver.getText("//span[@class='store-name']")
            time.sleep(1)
        self.writeFile(result)
    def writeFile(self,result):

        path = 'kebuke_branch.csv'  # output FileName
        with open(path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in result:
                writer.writerow([i])






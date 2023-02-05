import scrapy
import re

class TopCVSprider(scrapy.Spider):
    name = 'topcv'
    allowed_domains = ['www.topcv.vn']
    
    start_urls = [
        #'https://www.topcv.vn/viec-lam/-/890384.html',
    ]

    for i in range(890384):
        start_urls.append(f'https://www.topcv.vn/viec-lam/-/{890384 - i}.html')

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

        self.count = 890384
        self.pattern = "^(https:\/\/www\.topcv\.vn\/viec-lam\/)([a-z0-9A-Z\-]{1,}\/)([0-9]{1,})(\.html)"

    def preprocessText(self, text) -> str:
        if text is None:
            return ''
        
        return ''.join(e for e in text if ((e.isalnum() or e.isspace() or e == '\\' or e == '/') 
                and e != '\n' and e != '\xa0'))

    def getNext(self):
        self.count -= 1
        return scrapy.Request(url=f'https://www.topcv.vn/viec-lam/-/{self.count}.html', callback=self.parse)

    def parse(self, response):
        if re.match(self.pattern, response.request.url):
            locations = []
            for div in response.xpath("//*[@style='margin-bottom: 10px']/text()"):
                text = self.preprocessText(div.get())
                if text and not text.isspace():
                    locations.append(text)

            descs = []
            for div in response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[3]/div[1]//text()'):
                text = self.preprocessText(div.get())
                if text and not text.isspace():
                    descs.append(text)

            requirementDescs = []
            for div in response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[3]/div[2]//text()'):
                text = self.preprocessText(div.get())
                if text and not text.isspace():
                    requirementDescs.append(text)

            benefitDescs = []
            for div in response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[3]/div[3]//text()'):
                text = self.preprocessText(div.get())
                if text and not text.isspace():
                    benefitDescs.append(text)

            types = []
            for div in response.xpath('//*[@id="tab-info"]/div/div/div[2]/div[3]/div[1]/span/a/text()'):
                text = self.preprocessText(div.get())
                if text and not text.isspace():
                    types.append(text)

            yield {
                'url'                     : response.request.url,
                'CompanyName'             : self.preprocessText(response.xpath('//*[@id="job-detail-page-wraper"]/div[2]/div[2]/div[1]/div[1]/div/a/text()').get()),
                'CompanyImage'            : response.xpath('//*[@id="job-detail-page-wraper"]/div[2]/div[2]/div[1]/a/div/img/@src').get(),
                'Salary'                  : self.preprocessText(response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[1]/div/div[1]/div/span/text()').get()),
                'AvaiableSlots'           : self.preprocessText(response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[1]/div/div[2]/div/span/text()').get()),
                'WorkingType'             : self.preprocessText(response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[1]/div/div[3]/div/span/text()').get()),
                'Position'                : self.preprocessText(response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[1]/div/div[4]/div/span/text()').get()),
                'SexRequirement'          : self.preprocessText(response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[1]/div/div[5]/div/span/text()').get()),
                'ExperimentRequirement'   : self.preprocessText(response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[1]/div/div[6]/div/span/text()').get()),
                'Locations'               : locations,
                'JobDescriptions'         : descs,
                'RequirementDescriptions' : requirementDescs,
                'BenefitDescriptions'     : benefitDescs,
                'Deadline'                : self.preprocessText(response.xpath('//*[@id="tab-info"]/div/div/div[1]/div[3]/div[4]/div/div/p/text()').get()),
                'Type'                    : types
            }

        #if self.count > 0:
        #    print('=============================================================================================')
        #    yield self.getNext()

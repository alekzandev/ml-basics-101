import pandas as pd
import ssl

class GetData:
    def __init__(self, url_data: str):
        self.url_data = url_data
        self.df: pd.DataFrame = None

    def get_data(self):
        self.df = pd.read_csv(self.url_data)
        
    def export_data(self):
        self.df.to_csv('data.csv', index = False)


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    url_data = "https://storage.googleapis.com/kagglesdsdata/datasets/2355600/4097760/House_Rent_Dataset.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220913%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220913T014147Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=070b888682c60fd5adb70da53c9c02b512010baf93aca5e86984c182066ec19c094e71dbfbd99c572c6b41fd17b239921a3f2b55052cd62657493a3af492c1e71ba4622c59622f2d5ff089e6d0f3cf64a5d293b935c903794ba1d140917452d303eab3030980116da07f8c18321a5dba37b23e82991fe82c632acbc071cdfb109eeb9462c7de19c2b9e44afa40198a3576de0e71e7423cf5e20d6534d7bd0a160810fe1e14501baedf3434e5936152c070f43b4ca99473ee29a3367b8ca45dffe4658da68c63d01954cfb4a91a737fa7b2675d9f0ea28682af128695da782347736d28ce1190dcdcfa4ba07987ce7577c22422c1d55090d26f165eb62f96b95d"
    getdata = GetData(url_data)
    getdata.get_data()
    getdata.export_data()

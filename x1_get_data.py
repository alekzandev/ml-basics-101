import pandas as pd

class GetData:
    
    def __init__(
        self,
        url_data: str
        ):
        self.url_data = url_data
        self.df: pd.DataFrame = None

    def get_data(self):
        #response = requests.get(self.url_data)
        #self.df = pd.read_csv(response.text, sep=',')
        self.df = pd.read_csv(self.url_data)

if __name__ == "__main__":
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    url_data = "https://storage.googleapis.com/kagglesdsdata/datasets/2355600/4097760/House_Rent_Dataset.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220907%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220907T042446Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=71cd3808468948c2227bdd2f3cc7c20a129704c8e85a3f9270f89c30974fc1b68a7c6072e7d787265b84517d23b1d6e9be5d85de0bbade97f51f951301f53614dd8c0e2ff4e9c1f114de99e5737aff7eb48e6ead6d8e905a9051abf584f8cc94af8ac797d0e9333b79eceb42638e64f3468ed1b314c177866e020f5adf18b2d50a62f557b9ec1db024a048c8dece3ffa9038e25e18fe12a46d56bcb4f538ccc11081de3f0f1a0545a7b7583a7e7947e8020f41abb3be1338dabcccc72383cd368cceb32fedfe01ab1386fbfe4acc3550d6df214af073b5116e8e17b1d50fb6a3e8ac20adba6226f869deb5a02020c64928d6ef7c39373540ec4bc017de41023d"
    get_data = GetData(url_data)
    get_data.get_data()
    print(get_data.df.head())
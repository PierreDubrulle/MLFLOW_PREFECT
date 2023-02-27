import random, json, os, requests
from collections import defaultdict
from schedule import every, repeat, run_pending

class generate_data():

    def __init__(self) -> None:

        self.var = ['poids', 'age', 'sexe', 'taille', 'ant_famille', 'CSP', 'Maladie']
        self.CSP = ['basse', 'moyenne', 'superieure']
        self.nb_lines = 200
        self.data = defaultdict(dict)
        self.filename = './data.json'
        self.new_lines = 50
    
    def random_data(self, first_line=1, last_line=5000) -> str:

        self.start = first_line
        self.stop = last_line

        for id in range(self.start, self.stop):
            for key in self.var:
                if key == 'poids':
                    self.data[id][key] = round(random.uniform(40,120), 2)
                if key == 'age':
                    self.data[id][key] = random.randrange(18,85,1)
                if key == 'sexe':
                    self.data[id][key] = str(random.choice(['F', 'M']))
                if key == 'taille':
                    self.data[id][key] = round(random.uniform(150,205), 2)
                if key == 'ant_famille':
                    self.data[id][key] = str(random.choices(['O','N'], weights=[30,70])[0])
                if key == 'Maladie':
                    self.data[id][key] = str(random.choices(['O','N'], weights=[10,90])[0])
                if key == 'CSP':
                    self.data[id][key] = random.choice(self.CSP)
        
        json_data = json.dumps(self.data, indent=4)
        return json_data
   

    def seed_file(self) -> dict:

        if os.path.isfile(self.filename) is not True:

            with open(self.filename, 'w') as f:

                self.data_to_write = self.random_data()
                f.write(self.data_to_write)

        else:

            with open(self.filename, 'r') as f:

                self.old_data = json.load(f)
                
                self.last_key = int(list(self.old_data.keys())[-1]) + 1

                self.new_data = self.random_data(self.last_key, self.last_key + int(self.new_lines))

                self.real_data = {**self.old_data, **json.loads(self.new_data)}

                self.real_data = json.dumps(self.real_data, indent=4)
                
            with open(self.filename, 'w') as f:

                f.write(self.real_data)

    
    def send_api(self):
        with open(self.filename, 'rb') as f:
            requests.post('http://server:8000/uploadfile/', files={'file':f})


@repeat(every().minutes)
def main():
    data = generate_data()
    data.random_data()
    data.seed_file()
    data.send_api()

if __name__ == '__main__':
    while(True):
        run_pending()



    
    







import pathlib
import json

DIR_ACTUAL = pathlib.Path(__file__).parent.absolute() #La direccion actual

def save_json_data( json_data , nombre , dir_carp ):
    with open( dir_carp/f'{nombre}.json', 'w' , encoding='utf-8' ) as file:
        json.dump( json_data , file, indent=2 , ensure_ascii= False ) #utf8



if __name__ == "__main__":    
    save_json_data( {"Diego":"Cazon"} , "file1" , DIR_ACTUAL )
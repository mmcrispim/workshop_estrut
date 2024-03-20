import pandas as pd
import os

def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:

    """
    receber um dataframe e salvar como excel

    args: 
    data_frame (pd.DataFrame): dataframe a ser salvo como excel
    output_path (str): caminho onde o arquivo será salvo
    file_name (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"
    """

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"

# if __name__ == "__main__":
#     df = pd.dataframe({'col1':[1,2], 'col2':[3,4]})
#     print(load_excel(df, "data/output", "test"))
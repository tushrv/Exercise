import pandas as pd
from typing import List


columns = ['student_id', 'age']
DF = pd.DataFrame({'student_id': [101,102,103,104],'name':['Ulysses','William','Henry','Henry'],'age':[13,10,6,11]})

def createDataframe_from_list(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=columns)


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players),len(players.columns)]

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(n=3)


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    sub_df = students[students['student_id']==101][['name','age']]

    return sub_df

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['age'].apply(lambda x: x*2)

    return employees

if __name__ == '__main__':
    student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
    ]
    print(createDataframe_from_list(student_data=student_data))
    
    print(getDataframeSize(DF))
    print(selectFirstRows(DF))
    print(selectData(DF))
    print(createBonusColumn(DF))
    
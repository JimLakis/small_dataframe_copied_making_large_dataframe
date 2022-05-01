import pandas as pd


class ConcatCopyOfDfs:
    def __init__(self, df1: pd.DataFrame, number_of_copies: int):
        self._df1 = df1
        self._df2 = df1
        self._number_of_copies = number_of_copies
    
    @property
    def new_df(self):
        if self._number_of_copies == 1:
            return self._df1
        elif self._number_of_copies > 1:
            counter = 0
            while counter < self._number_of_copies - 1:
                self._df1 = pd.concat([self._df1, self._df2], ignore_index=True)
                counter += 1
            return self._df1
    
    def __str__(self):
        return f'{self.new_df}'

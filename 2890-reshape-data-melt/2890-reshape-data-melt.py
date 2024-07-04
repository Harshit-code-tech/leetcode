import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
  id_vars = report.columns[0]
  melted_df = report.melt(id_vars=id_vars, var_name='quarter', value_name='sales')

  return melted_df
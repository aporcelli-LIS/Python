{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    OBJECTID_12_13  OBJECTID  DEPCODE  COUNTY  COUNTYNAME  \\\n",
      "0                1         1       21      41   GILCHRIST   \n",
      "1                2         2       54     107      PUTNAM   \n",
      "2                3         3       62     123      TAYLOR   \n",
      "3                4         4       46      91    OKALOOSA   \n",
      "4                5         5        7      13     CALHOUN   \n",
      "..             ...       ...      ...     ...         ...   \n",
      "63              64        64       47      93  OKEECHOBEE   \n",
      "64              65        65       19      37    FRANKLIN   \n",
      "65              66        66        1       1     ALACHUA   \n",
      "66              67        67       55     109   ST. JOHNS   \n",
      "67              68       999      999     999     Unknown   \n",
      "\n",
      "                   DATESTAMP    ShapeSTAre    ShapeSTLen  OBJECTID_1  \\\n",
      "0   2000-05-16T00:00:00.000Z  9.908353e+09  4.873000e+05          21   \n",
      "1   2000-05-16T00:00:00.000Z  2.305869e+10  7.629677e+05          54   \n",
      "2   2000-05-16T00:00:00.000Z  2.891747e+10  8.772527e+05          62   \n",
      "3   2000-05-16T00:00:00.000Z  2.562159e+10  1.087058e+06          46   \n",
      "4   2000-05-16T00:00:00.000Z  1.604809e+10  6.313440e+05           7   \n",
      "..                       ...           ...           ...         ...   \n",
      "63  2000-05-16T00:00:00.000Z  2.484427e+10  8.939740e+05          47   \n",
      "64  2000-05-16T00:00:00.000Z  1.558955e+10  1.467125e+06          19   \n",
      "65  2000-05-16T00:00:00.000Z  2.702324e+10  8.927266e+05           1   \n",
      "66  2000-05-16T00:00:00.000Z  1.784792e+10  1.130720e+06          58   \n",
      "67                       NaN           NaN           NaN          64   \n",
      "\n",
      "      County_1  ... T_negative  T_pending  T_positive  FLandNonFLDeaths  \\\n",
      "0    Gilchrist  ...          7          0           0                 0   \n",
      "1       Putnam  ...         81         28           2                 0   \n",
      "2       Taylor  ...         12          0           0                 0   \n",
      "3     Okaloosa  ...         62         15          14                 0   \n",
      "4      Calhoun  ...          6          0           0                 0   \n",
      "..         ...  ...        ...        ...         ...               ...   \n",
      "63  Okeechobee  ...         17          4           0                 0   \n",
      "64    Franklin  ...         11          0           0                 0   \n",
      "65     Alachua  ...        590         42          37                 0   \n",
      "66   St. Johns  ...        243         26          22                 1   \n",
      "67     Unknown  ...          4          0           0                 0   \n",
      "\n",
      "    EverMon  MonNow   Shape__Area  Shape__Length   Shape_Length    Shape_Area  \n",
      "0         0       0  9.204908e+08  148547.348006  148547.347588  9.204908e+08  \n",
      "1         0       0  2.142439e+09  232574.925675  232574.926296  2.142439e+09  \n",
      "2         0       0  2.685253e+09  267348.178950  267348.178429  2.685253e+09  \n",
      "3        58      16  2.369223e+09  330553.160278  330553.159869  2.369223e+09  \n",
      "4         0       0  1.487627e+09  192207.890331  192207.890041  1.487627e+09  \n",
      "..      ...     ...           ...            ...            ...           ...  \n",
      "63        1       1  2.307691e+09  272539.677334  272539.676296  2.307691e+09  \n",
      "64        0       0  1.445841e+09  446544.245992  446544.245391  1.445841e+09  \n",
      "65       11       1  2.510756e+09  272135.471452  272135.471806  2.510756e+09  \n",
      "66       19       4  1.658207e+09  344848.248220  344848.248780  1.658207e+09  \n",
      "67        2       1  4.267574e+08   73231.292129   73231.292129  4.267574e+08  \n",
      "\n",
      "[68 rows x 89 columns]\n"
     ]
    }
   ],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import filedialog\n",
    "import pandas as pd\n",
    "\n",
    "root= tk.Tk()\n",
    "\n",
    "canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')\n",
    "canvas1.pack()\n",
    "\n",
    "def getExcel ():\n",
    "    global df\n",
    "    \n",
    "    import_file_path = filedialog.askopenfilename()\n",
    "    df = pd.read_excel (import_file_path)\n",
    "    print (df)\n",
    "    \n",
    "browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))\n",
    "canvas1.create_window(150, 150, window=browseButton_Excel)\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

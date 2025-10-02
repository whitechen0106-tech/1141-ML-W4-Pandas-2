# -*- coding: utf-8 -*-
"""
Pandas 基礎操作課堂練習：學生期中成績分析
"""

import pandas as pd

def load_and_explore_data(file_path):
    """任務一：讀取 CSV 並初步探索資料"""
    df = pd.read_csv(file_path, encoding='utf-8-sig')
    
    # TODO 1.1: 顯示前 5 筆資料
    print(df.head(), "\n")

    # TODO 1.2: 查看資料結構（欄位、型態、缺失值）
    print(df.info())
    print("\n缺失值統計：")
    print(df.isnull().sum(), "\n")

    return df

def feature_engineering(df):
    """任務二：計算總分、平均分數與是否及格"""
    
    # TODO 2.1: 計算總分
    df["總分"] = df[[ "數學", "國文", "英文", "自然", "社會"]].sum(axis=1)
    print(df[["姓名","數學", "國文", "英文", "自然", "社會","總分"]], "\n")

    # TODO 2.2: 計算平均分數
    df["平均"] = df[["數學", "國文", "英文", "自然", "社會"]].mean(axis=1)
    print(df[["姓名","總分","平均"]], "\n")

    # TODO 2.3: 新增是否及格欄位（平均 >= 60 為及格）
    df["是否及格"] = df["平均"] >= 60
    print(df[["姓名","平均","是否及格"]], "\n")

    return df 

def filter_and_analyze_data(df):
    """任務三與四：篩選資料與統計"""
    
    # TODO 3.1: 找出數學成績 < 60 的學生
    math_failed = df[df["數學"] < 60]
    print(math_failed, "\n")

    # TODO 3.2: 找出班級為 'A' 且英文 > 90 的學生
    high_A = df[(df["班級"] == "A") & (df["英文"] > 90)]
    print(high_A, "\n")

    # TODO 4.1: 統計摘要
    summary = df.describe()
    print(summary, "\n")

    # TODO 4.2: 找出總分最高的學生
    top_student = df.loc[df["總分"].idxmax()]
    print(top_student, "\n")

    return {
        "processed_df": df,
        "math_failed": math_failed,
        "high_A": high_A,
        "summary": summary,
        "top_student": top_student
    }

def save_results(df, output_file_path):
    """任務五：儲存為 CSV"""
    
    # TODO 5.1: 儲存 CSV，避免中文亂碼
    df.to_csv(output_file_path, index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    INPUT_CSV = "grades.csv"
    OUTPUT_CSV = "grades_analyzed.csv"

    df = load_and_explore_data(INPUT_CSV)
    df = feature_engineering(df)
    result = filter_and_analyze_data(df)
    save_results(result["processed_df"], OUTPUT_CSV)

    print("完成所有分析任務")

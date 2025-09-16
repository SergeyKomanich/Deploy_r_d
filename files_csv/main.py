"""
FIFA PLAYERS ANALYSIS - ДИПЛОМНА РОБОТА
=======================================
Комплексний аналіз даних футбольних гравців з використанням Data Science методів

Структура проекту:
├── main.py                 (цей файл - головний запуск)
├── src/
│   ├── data_loader.py      (завантаження та первинна обробка даних)
│   ├── analytical_block.py (завдання 1-7: аналітичні запити)
│   ├── visualization_block.py (завдання 8-10: візуалізації)
│   ├── analytical_thinking.py (завдання 11-15: метрики та аналіз)
│   ├── business_analytics.py (завдання 16: бізнес-інсайти)
│   ├── eda_feature_engineering.py (завдання 17-19: EDA + Feature Engineering)
│   └── modeling.py         (завдання 20: машинне навчання)
├── data/
│   └── player-data-full-2025-june.csv
├── results/
│   ├── plots/              (збережені графіки)
│   ├── reports/            (текстові звіти)
│   └── models/             (збережені моделі)
└── requirements.txt        (залежності)

Автор: [Ваше ім'я]
Курс: Data Science
Рік: 2025
"""

import sys
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Додаємо шлях до src модулів
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def create_project_structure():
    """Створення структури директорій проекту"""
    dirs = ['src', 'data', 'results', 'results/plots', 'results/reports', 'results/models']
    
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    
    print("📁 Структура проекту створена!")

def main():
    """Головна функція - запуск всіх блоків аналізу"""
    
    print("🚀 FIFA PLAYERS ANALYSIS - ДИПЛОМНА РОБОТА")
    print("=" * 60)
    print("Комплексний аналіз даних футбольних гравців")
    print("Data Science курс | 2025")
    print("=" * 60)
    
    # Створюємо структуру проекту
    create_project_structure()
    
    try:
        # Імпортуємо модулі
        from data_loader import DataLoader
        from analytical_block import AnalyticalBlock
        from visualization_block import VisualizationBlock
        from analytical_thinking import AnalyticalThinking
        from business_analytics import BusinessAnalytics
        from eda_feature_engineering import EDAFeatureEngineering
        from modeling import ModelingBlock
        
        # Завантаження та підготовка даних
        print("\n📥 БЛОК 0: ЗАВАНТАЖЕННЯ ТА ПІДГОТОВКА ДАНИХ")
        print("-" * 50)
        loader = DataLoader()
        df = loader.load_and_prepare_data()
        
        if df is None:
            print("❌ Не вдалося завантажити дані. Перевірте наявність файлу.")
            return
        
        # БЛОК 1: Аналітичні завдання (1-7)
        print("\n🔍 БЛОК 1: АНАЛІТИЧНІ ЗАВДАННЯ (10 БАЛІВ)")
        print("-" * 50)
        analytical = AnalyticalBlock(df)
        analytical.run_all_tasks()
        
        # БЛОК 2: Візуалізації (8-10)
        print("\n📊 БЛОК 2: ВІЗУАЛІЗАЦІЇ (3 БАЛИ)")
        print("-" * 50)
        visualization = VisualizationBlock(df)
        visualization.run_all_visualizations()
        
        # БЛОК 3: Аналітичне мислення (11-15)
        print("\n🧠 БЛОК 3: АНАЛІТИЧНЕ МИСЛЕННЯ (7 БАЛІВ)")
        print("-" * 50)
        thinking = AnalyticalThinking(df)
        thinking.run_all_analysis()
        
        # БЛОК 4: Бізнес аналітика (16)
        print("\n💼 БЛОК 4: БІЗНЕС АНАЛІТИКА (5 БАЛІВ)")
        print("-" * 50)
        business = BusinessAnalytics(df)
        business.generate_business_insights()
        
        # БЛОК 5: EDA + Feature Engineering (17-19)
        print("\n🔬 БЛОК 5: EDA + FEATURE ENGINEERING (15 БАЛІВ)")
        print("-" * 50)
        eda = EDAFeatureEngineering(df)
        processed_df = eda.run_full_eda_pipeline()
        
        # БЛОК 6: Моделювання (20)
        print("\n🤖 БЛОК 6: МАШИННЕ НАВЧАННЯ (15 БАЛІВ)")
        print("-" * 50)
        modeling = ModelingBlock(processed_df)
        modeling.run_modeling_pipeline()
        
        # Підсумкове звітування
        print("\n📋 ПІДСУМОК ПРОЕКТУ")
        print("=" * 60)
        print("✅ Блок 1 (Аналітика): 10 балів")
        print("✅ Блок 2 (Візуалізації): 3 бали")
        print("✅ Блок 3 (Аналітичне мислення): 7 балів")
        print("✅ Блок 4 (Бізнес аналітика): 5 балів")
        print("✅ Блок 5 (EDA + Feature Engineering): 15 балів")
        print("✅ Блок 6 (Моделювання): до 15 балів")
        print("-" * 60)
        print("🎯 ВСЬОГО: до 55 балів")
        print("📁 Результати збережено в папку 'results/'")
        print("🎉 ПРОЕКТ ЗАВЕРШЕНО УСПІШНО!")
        
    except ImportError as e:
        print(f"❌ Помилка імпорту модуля: {e}")
        print("Створіть файли модулів в папці 'src/'")
        return
    except Exception as e:
        print(f"❌ Помилка виконання: {e}")
        return

if __name__ == "__main__":
    main()
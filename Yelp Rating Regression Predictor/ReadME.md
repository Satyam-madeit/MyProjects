# 🍽️ Yelp Rating Regression Predictor

A machine learning project that predicts Yelp star ratings for restaurants using Linear Regression, trained on real Yelp dataset features.

---

## 📁 Dataset

The project uses six Yelp JSON files:
[Click to download the zip file of the data](https://content.codecademy.com/programs/machine-learning/cumulative-projects/yelp_regression_project.zip?_gl=1*1a6ft6x*_gcl_au*Mzk0MzQ3NzAwLjE3NzI4MjEwMDY.*_ga*MjkyMjQyMzM0MC4xNzQ1OTMzOTEy*_ga_3LRZM6TM9L*czE3NzM1OTI2NzMkbzExMSRnMSR0MTc3MzU5NDQxMiRqNDkkbDAkaDA.)

| File | Description |
|------|-------------|
| `yelp_business.json` | Business location and attribute data |
| `yelp_review.json` | Review metadata by business |
| `yelp_user.json` | User profile metadata by business |
| `yelp_checkin.json` | Online check-in metadata by business |
| `yelp_tip.json` | Tip metadata by business |
| `yelp_photo.json` | Photo metadata by business |

---

## 🔄 Project Workflow

### Section 1 — Data Preview & Cleaning
- **Step 1:** Load all six JSON files into individual DataFrames and preview each
- **Step 2:** Merge all DataFrames on `business_id` using left joins, then drop nulls and irrelevant columns (e.g. address, city, coordinates)

### Section 2 — Preparation for Model Training
- **Step 3:** Compute and visualize a **correlation heatmap** to understand feature relationships
- **Step 4:** Plot key relationships (stars vs review sentiment, fans, kid-friendliness)

### Section 3 — Training the Model
- **Step 5:** Define feature matrix `X` (24 features) and target `y` (stars), split 80/20 train-test
- **Step 6:** Train a **Linear Regression** model and generate predictions
- **Step 7:** Evaluate — initial model score: **~66.7%**

### Section 4 — Tuning the Model
- **Step 8:** Inspect feature coefficients to identify low-impact features
- **Step 9:** Drop 9 near-zero features and retrain
- **Step 10:** Re-evaluate — improved model score: **~71%**

### Section 5 — Real-World Test
- Test the model on an imaginary restaurant: **Satyam's Kitchen**
- Predicted rating: **4.29 ⭐**

---

## ✅ Features Used (Final Model)

After removing low-impact features, the final model uses:

```
alcohol?, good_for_kids, has_bike_parking, has_wifi, is_open,
price_range, take_reservations, takes_credit_cards,
average_review_length, average_review_sentiment,
number_cool_votes, number_tips, average_number_fans,
average_review_count, average_number_years_elite
```

> 💡 `average_review_sentiment` has the highest coefficient (~2.50) — it is by far the strongest predictor of star rating.

---

## 🧪 Test with Your Own Restaurant

```python
import numpy as np

your_restaurant = np.array([[
    0,      # alcohol?                  (0 = No, 1 = Yes)
    1,      # good_for_kids             (0 = No, 1 = Yes)
    1,      # has_bike_parking          (0 = No, 1 = Yes)
    1,      # has_wifi                  (0 = No, 1 = Yes)
    1,      # is_open                   (0 = No, 1 = Yes)
    2,      # price_range               (1 = cheap → 4 = expensive)
    1,      # take_reservations         (0 = No, 1 = Yes)
    1,      # takes_credit_cards        (0 = No, 1 = Yes)
    150,    # average_review_length     (characters)
    0.8,    # average_review_sentiment  (-1 to 1)
    10,     # number_cool_votes
    5,      # number_tips
    20,     # average_number_fans
    50,     # average_review_count
    2,      # average_number_years_elite
]])

predicted_stars = regr.predict(your_restaurant)
print(f"Predicted Star Rating: {predicted_stars[0][0]:.2f} ⭐")
```

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — data loading, merging, cleaning
- **Matplotlib & Seaborn** — data visualization
- **Scikit-learn** — Linear Regression, train-test split, model evaluation
- **NumPy** — array handling for predictions

---

## 📊 Model Performance

| Version | Features | R² Score |
|---------|----------|----------|
| Initial | 24 | ~66.7% |
| Tuned | 15 | ~74.4% |

---

## 🚀 How to Run

1. Place all six Yelp JSON files in the project directory
2. Open `main.ipynb` in Jupyter Notebook or VS Code
3. Run all cells in order
4. Modify the restaurant values in Section 5 to test your own inputs

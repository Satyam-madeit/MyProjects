# 🎬 Netflix Content Analysis

> A comprehensive data analysis exploring Netflix's content strategy through genre, geographic, and temporal trends

## 📊 Overview

This project analyzes **8,807 Netflix titles** to uncover strategic insights about the platform's content distribution, revealing patterns in genre preferences, geographic diversity, and content acquisition strategies.

### Key Findings

- **97.2%** of Netflix's catalog consists of movies
- **62%** of content is international (non-US)
- **42%** of genre tags are international-related
- **2017-2018** marked peak content acquisition
- **TV-MA** content leads at 38% of catalog

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/netflix-analysis.git
cd netflix-analysis

# Install dependencies
pip install pandas matplotlib numpy

# Run the analysis
jupyter notebook netflix_analysis_improved.ipynb
```

## 📁 Project Structure

```
netflix-analysis/
│
├── netflix_analysis_improved.ipynb    # Main analysis notebook
├── netflix_titles.csv                 # Dataset (not included)
├── README.md                          # This file
```

## 🔍 Analysis Sections

1. **Data Loading & Exploration** - Initial dataset examination
2. **Data Cleaning** - Handling missing values and duplicates
3. **Content Type Analysis** - Movies vs. TV Shows distribution
4. **Temporal Trends** - Release year patterns
5. **Geographic Distribution** - Country-wise content analysis
6. **Maturity Ratings** - Rating distribution insights
7. **Genre Deep Dive** - Genre trends and combinations
8. **Business Recommendations** - Strategic insights for Netflix

## 📈 Visualizations

The notebook includes **8 comprehensive visualizations**:

- Content type distribution (pie & bar charts)
- Release year trends with statistical indicators
- Top 15 countries by content volume
- Maturity rating distribution
- Top 15 genres analysis
- Genre combinations heat analysis
- Genre evolution over time
- Movies vs. TV Shows genre comparison

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **NumPy** - Numerical operations
- **Jupyter Notebook** - Interactive development environment

## 📊 Dataset

The analysis uses the Netflix Movies and TV Shows dataset containing:
- 8,807 titles (cleaned to 5,332)
- 12 columns including title, director, cast, country, rating, genre, etc.
- Data spanning from 1925 to 2021

**Note:** Dataset not included in repository. Download from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).

## 💡 Key Insights

### Strategic Positioning
- Movie-dominant platform with 97.2% films
- Strong international content strategy (62% non-US)
- Adult content differentiation (41% mature-rated)

### Business Recommendations
1. **Diversify TV show portfolio** from 2.8% to 15-20%
2. **Leverage international content** success
3. **Balance mature and family content**
4. **Optimize genre combinations** for better discoverability
5. **Address content recency gap** in 2020-2021

## 📝 Requirements

```
pandas>=2.0.0
matplotlib>=3.0.0
numpy>=1.20.0
jupyter>=1.0.0
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new analyses
- Improve visualizations
- Add new features

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Satyam Srivastava**
- GitHub: [Satyam-madeit](https://github.com/Satyam-madeit)

## 🙏 Acknowledgments

- Netflix for inspiring this analysis
- Kaggle for providing the dataset
- The open-source community

---

Made with ❤️ and Python

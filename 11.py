# 小红书NLP增强分析（结合04.md的RFM模型）
def xhs_sentiment_analysis(notes):
    # 使用ERNIE3.0模型（知识库技术）进行细粒度情感分析
    sentiments = ernie.analyze([n['content'] for n in notes])
    
    # 热度公式（05.md数据可视化规范）
    hot_score = (点赞数 * 0.4 + 收藏数 * 0.3 + 评论数 * 0.3) * 情感极性系数
    
    # 话题聚类（03.md物流预测模型改造）
    clusters = BERTopic().fit_transform([n['content'] for n in notes])
    return pd.DataFrame({热点话题:clusters, 情感分:sentiments, 热度:hot_score})

# 抖音转化率关联分析（API数据对接）
def dy_correlation(xhs_data):
    # 通过抖音橱窗API获取实时转化数据
    dy_data = DouyinAPI.get_product_stats()
    
    # 构造关联矩阵（应用05.md数据对比图表）
    merged_df = pd.merge(xhs_data, dy_data, on='product_id')
    return merged_df.corr(method='spearman')[['加购率','成交率']]
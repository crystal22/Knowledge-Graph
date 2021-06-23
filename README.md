# 基于知识图谱的推荐系统

### 基于嵌入的方法

##### item graph

| 方法       | 年份 | 论文                                                         | 源码                                 |
| ---------- | ---- | ------------------------------------------------------------ | ------------------------------------ |
| CKE        | 2016 | Collaborative  knowledge base embedding for recommender systems |                                      |
| DKN        | 2018 | Deep  Knowledge-Aware Network for News Recommendation        | https://github.com/hwwang55/DKN      |
| KSR        | 2018 | Improving  Sequential Recommendation with Knowledge-Enhanced Memory Networks | https://github.com/RUCDM/KSR         |
| entity2rec | 2017 | Entity2rec:  learning user-item relatedness from knowledge graphs for top-n item  recommendation | https://github.com/D2KLab/entity2rec |

##### user-item graph

| 方法  | 年份 | 论文                                                         | 源码                                                    |
| ----- | ---- | ------------------------------------------------------------ | ------------------------------------------------------- |
| CFKG  | 2018 | Learning Heterogeneous  Knowledge Base Embeddings for Explainable Recommendation | https://github.com/evison/KBE4ExplainableRecommendation |
| SHINE | 2018 | Signed  Heterogeneous Information Network Embedding for Sentiment Link Prediction |                                                         |
| DKFM  | 2019 | Location  embeddings for next trip recommendation            |                                                         |

##### 其他方法

| 方法  | 年份 | 论文                                                         | 源码                              |
| ----- | ---- | ------------------------------------------------------------ | --------------------------------- |
| KTGAN | 2018 | A  knowledge-enhanced deep recommendation framework incorporating gan-based  models | https://github.com/ZikaiGuo/KTGAN |
| BEM   | 2019 | Bayes EMbedding  (BEM): Refining Representation by Integrating Knowledge Graphs and  Behavior-specific Networks |                                   |
| RCF   | 2019 | Relational  collaborative filtering: Modeling multiple item relations for recommendation |                                   |

### 基于路径的方法

##### path连通性

| 方法      | 年份 | 论文                                                         | 源码                                  |
| --------- | ---- | ------------------------------------------------------------ | ------------------------------------- |
| FMG       | 2017 | Meta-graph based  recommendation fusion over heterogeneous information networks | https://github.com/HKUST-KnowComp/FMG |
| Hete-MF   | 2013 | Collaborative  filtering with entity similarity regularization in heterogeneous information  networks |                                       |
| HeteRec   | 2013 | Recommendation  in heterogeneous information networks with implicit user feedback |                                       |
| HeteRec_p | 2014 | Personalized  entity recommendation: A heterogeneous information network approach |                                       |
| Hete-CF   | 2014 | Hete-cf: Social-based  collaborative filtering recommendation using heterogeneous relations |                                       |
| SemRec    | 2015 | Semantic path  based personalized recommendation on weighted heterogeneous information  networks |                                       |
| HERec     | 2018 | Heterogeneous information  network embedding for recommendation | https://github.com/librahu/HERec      |
| RuleRec   | 2019 | Jointly learning  explainable rules for recommendation with knowledge graph | https://github.com/THUIR/RuleRec      |

##### path嵌入

| 方法  | 年份 | 论文                                                         | 源码                                                         |
| ----- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| MCRec | 2018 | Leveraging  metapath based context for top-n recommendation with a neural co-attention  model | https://github.com/librahu/MCRec                             |
| RKGE  | 2019 | Recurrent  knowledge graph embedding for effective recommendation | https://github.com/sunzhuntu/Recurrent-Knowledge-Graph-Embedding |
| KPRN  | 2019 | Explainable reasoning  over knowledge graphs for recommendation | https://github.com/xiangwang1223/KPRN    https://github.com/terwilligers/knowledge-graph-recommender |
| PGPR  | 2019 | Reinforcement  knowledge graph reasoning for explainable recommendation | https://github.com/orcax/PGPR   https://github.com/Jindiande/PGPR_conv2d |
| EIUM  | 2019 | Explainable interaction-driven  user modeling over knowledge graph for sequential recommendation |                                                              |
| Ekar  | 2019 | Explainable  knowledge graph-based recommendation via deep reinforcement learning | https://github.com/DeepGraphLearning/RecommenderSystems      |

### 联合方法

##### 基于user历史行为

| 方法      | 年份 | 论文                                                         | 源码                                                         |
| --------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| RippleNet | 2018 | Ripplenet:  Propagating user preferences on the knowledge graph for recommender systems | [https://github.com/hwwang55/RippleNet ](https://github.com/hwwang55/RippleNet) |
| AKUPM     | 2019 | Akupm:  Attentionenhanced knowledge-aware user preference model for recommendation |                                                              |
| RCoLM     | 2019 | Unifying  taskoriented knowledge graph learning and recommendation |                                                              |

##### 基于item多跳邻居

| 方法     | 年份 | 论文                                                         | 源码                                                         |
| -------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| KGCN     | 2019 | Knowledge graph  convolutional networks for recommender systems | [https://github.com/KanchiShimono/KGCN ](https://github.com/KanchiShimono/KGCN) |
| KGCN-LS  | 2019 | Knowledge-aware  graph neural networks with label smoothness regularization for recommender  systems |                                                              |
| KGAT     | 2019 | Kgat: Knowledge graph attention  network for recommendation  | [https://github.com/xiangwang1223/knowledge_graph_attention_network ](https://github.com/xiangwang1223/knowledge_graph_attention_network)[https://github.com/LunaBlack/KGAT-pytorch](https://github.com/LunaBlack/KGAT-pytorch)（包含CKE） |
| KNI      | 2019 | An end-to-end  neighborhood-based interaction model forknowledge-enhanced recommendation |                                                              |
| IntentGC | 2019 | Intentgc: a  scalable graph convolution framework fusing heterogeneous information for  recommendation | [https://github.com/peter14121/intentgc-models ](https://github.com/peter14121/intentgc-models) |

### 近年的一些方法

| 方法    | 年份 | 论文                                                         | 源码                                                         |
| ------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| M2GRL   | 2020 | M2GRL: A  Multi-task Multi-view Graph Representation Learning Framework for Web-scale  Recommender Systems | [https://github.com/99731/M2GRL ](https://github.com/99731/M2GRL) |
| LR-GCCF | 2020 | Revisiting Graph  based Collaborative Filtering : A Linear Residual Graph Convolutional Network  Approach | [https://github.com/newlei/LR-GCCF ](https://github.com/newlei/LR-GCCF) |
| MCCF    | 2020 | Multi-Component  Graph Convolutional Collaborative Filtering | [https://github.com/RuijiaW/Multi-Component-Graph-Convolutional-Collaborative-Filtering ](https://github.com/RuijiaW/Multi-Component-Graph-Convolutional-Collaborative-Filtering) |
| NGCF    | 2019 | Neural Graph  Collaborative Filtering                        | [https://github.com/xiangwang1223/neural_graph_collaborative_filtering ](https://github.com/xiangwang1223/neural_graph_collaborative_filtering) |
| MMGCN   | 2019 | Multi-modal Graph  Convolution Network for Personalized Recommendation of Micro-video | [https://github.com/weiyinwei/MMGCN ](https://github.com/weiyinwei/MMGCN) |
|         | 2019 | Graph-based-Recommendation-System                            | [https://github.com/YuxuanLongBeyond/Graph-based-Recommendation-System ](https://github.com/YuxuanLongBeyond/Graph-based-Recommendation-System)<br />[https://github.com/chandan-u/graph-based-recommendation-system ](https://github.com/chandan-u/graph-based-recommendation-system) |
| MKR     | 2019 | Multi-Task  Feature Learning for Knowledge Graph Enhanced Recommendation | [https://github.com/hwwang55/MKR ](https://github.com/hwwang55/MKR) |
| KBRD    | 2019 | Towards  Knowledge-Based Recommender Dialog System           | [https://github.com/THUDM/KBRD ](https://github.com/THUDM/KBRD) |




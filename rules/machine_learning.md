On extremely high dimensional data (I worked at a credit card processor company doing fraud modeling), deep learning dominates, but there's simply no advantage in using a designated "time series" model that treats time differently than any other feature. We've tried most time series deep learning models that claim to be SoTA - N-BEATS, N-HiTS, every RNN variant that was popular pre-transformers, and they don't beat an MLP that just uses lagged values as features. I've talked to several others in the forecasting space and they've found the same result.

On mid-dimensional data, LightGBM/Xgboost is by far the best and generally performs at or better than any deep learning model, while requiring much less finetuning and a tiny fraction of the computation time.

And on low-dimensional data, (V)ARIMA/ETS/Factor models are still king, since without adequate data, the model needs to be structured with human intuition.
https://news.ycombinator.com/item?id=37746921
https://news.ycombinator.com/item?id=37874891

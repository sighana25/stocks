{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red72\green139\blue206;
\red203\green203\blue202;\red212\green213\blue153;\red142\green213\blue255;\red213\green213\blue212;\red89\green155\blue61;
\red167\green197\blue151;\red194\green125\blue100;\red184\green111\blue179;\red115\green187\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c1\c1;\cssrgb\c100000\c100000\c99985;\cssrgb\c34356\c61927\c84546;
\cssrgb\c83411\c83410\c83098;\cssrgb\c86232\c86185\c66253;\cssrgb\c61728\c86919\c100000;\cssrgb\c86559\c86559\c86235;\cssrgb\c41351\c66031\c30488;
\cssrgb\c71061\c80852\c65647;\cssrgb\c80764\c56762\c46655;\cssrgb\c77483\c52772\c75312;\cssrgb\c51654\c78438\c100000;}
\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\deftab720
\pard\pardeftab720\sl380\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
def\cf2 \cb3  \cf2 \cb3 forecast_accuracy\cf2 \cb3 (\cf2 \cb3 forecast\cf2 \cb3 , \cf2 \cb3 actual\cf2 \cb3 , \cf2 \cb3 str_name\cf2 \cb3 )\cf2 \cb3 :\cf2 \cb3 \
    mape = np.mean\cf2 \cb3 (\cf2 \cb3 np.\cf2 \cb3 abs\cf2 \cb3 (\cf2 \cb3 forecast - actual\cf2 \cb3 )\cf2 \cb3 /np.\cf2 \cb3 abs\cf2 \cb3 (\cf2 \cb3 actual\cf2 \cb3 ))\cf2 \cb3  \cf2 \cb3 # MAPE\cf2 \cb3 \
    mae = np.mean\cf2 \cb3 (\cf2 \cb3 np.\cf2 \cb3 abs\cf2 \cb3 (\cf2 \cb3 forecast - actual\cf2 \cb3 ))\cf2 \cb3                  \cf2 \cb3 # MAE\cf2 \cb3 \
    rmse = np.mean\cf2 \cb3 ((\cf2 \cb3 forecast - actual\cf2 \cb3 )\cf2 \cb3 **\cf2 \cb3 2\cf2 \cb3 )\cf2 \cb3 **\cf2 \cb3 .5\cf2 \cb3                \cf2 \cb3 # RMSE\cf2 \cb3 \
    mse = np.mean\cf2 \cb3 ((\cf2 \cb3 forecast - actual\cf2 \cb3 )\cf2 \cb3 **\cf2 \cb3 2\cf2 \cb3 )\cf2 \cb3                     \cf2 \cb3 # MSE\cf2 \cb3 \
    df_acc = pd.DataFrame\cf2 \cb3 (\{\cf2 \cb3 'MAPE'\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 [\cf2 \cb3 mape\cf2 \cb3 ],\cf2 \cb3 \
                           \cf2 \cb3 'MAE'\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 [\cf2 \cb3 mae\cf2 \cb3 ],\cf2 \cb3 \
                           \cf2 \cb3 'RMSE'\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 [\cf2 \cb3 rmse\cf2 \cb3 ],\cf2 \cb3 \
                           \cf2 \cb3 'MSE'\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 [\cf2 \cb3 mse\cf2 \cb3 ],\cf2 \cb3  \
                           \cf2 \cb3 \},\cf2 \cb3 \
                          index=\cf2 \cb3 [\cf2 \cb3 str_name\cf2 \cb3 ])\cf2 \cb3 \
    \cf2 \cb3 return\cf2 \cb3  df_acc\
\
\cf2 \cb3 def\cf2 \cb3  \cf2 \cb3 ARIMA_forecast\cf2 \cb3 (\cf2 \cb3 serie_dates\cf2 \cb3 , \cf2 \cb3 serie\cf2 \cb3 , \cf2 \cb3 n_test\cf2 \cb3 , \cf2 \cb3 pq\cf2 \cb3 , \cf2 \cb3 d\cf2 \cb3 )\cf2 \cb3 :\cf2 \cb3 \
  n_serie=\cf2 \cb3 len\cf2 \cb3 (\cf2 \cb3 serie\cf2 \cb3 )\cf2 \cb3 \
  train_size = n_serie - n_test\
  train = serie.iloc\cf2 \cb3 [:\cf2 \cb3 train_size\cf2 \cb3 ]\cf2 \cb3 \
  test = serie.iloc\cf2 \cb3 [\cf2 \cb3 train_size\cf2 \cb3 :\cf2 \cb3 train_size + n_test\cf2 \cb3 ]\cf2 \cb3  \
  dates = serie_dates.iloc\cf2 \cb3 [\cf2 \cb3 train_size\cf2 \cb3 :\cf2 \cb3 train_size + n_test\cf2 \cb3 ]\cf2 \cb3 \
  best_aic = np.inf\
  best_bic = np.inf\
  best_order = \cf2 \cb3 None\cf2 \cb3 \
  best_mdl = \cf2 \cb3 None\cf2 \cb3 \
  pq_rng = \cf2 \cb3 range\cf2 \cb3 (\cf2 \cb3 pq\cf2 \cb3 )\cf2 \cb3  \cf2 \cb3 #resagos (autoregresivos)\cf2 \cb3 \
  d_rng  = \cf2 \cb3 range\cf2 \cb3 (\cf2 \cb3 d\cf2 \cb3 )\cf2 \cb3  \cf2 \cb3 #restar maximo 3 veces (diferenciaci\'f3n)\cf2 \cb3 \
  \cf2 \cb3 for\cf2 \cb3  i \cf2 \cb3 in\cf2 \cb3  pq_rng\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 #autoregresivos\cf2 \cb3 \
      \cf2 \cb3 for\cf2 \cb3  d \cf2 \cb3 in\cf2 \cb3  d_rng\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 #diferenciaci\'f3n\cf2 \cb3 \
          \cf2 \cb3 for\cf2 \cb3  j \cf2 \cb3 in\cf2 \cb3  pq_rng\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 #medias moviles\cf2 \cb3 \
              \cf2 \cb3 try\cf2 \cb3 :\cf2 \cb3 \
                  tmp_mdl = sm.tsa.ARIMA\cf2 \cb3 (\cf2 \cb3 train\cf2 \cb3 ,\cf2 \cb3  order=\cf2 \cb3 (\cf2 \cb3 i\cf2 \cb3 ,\cf2 \cb3 d\cf2 \cb3 ,\cf2 \cb3 j\cf2 \cb3 ))\cf2 \cb3 .fit\cf2 \cb3 (\cf2 \cb3 method_kwargs=\cf2 \cb3 \{\cf2 \cb3 "warn_convergence"\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 False\cf2 \cb3 \})\cf2 \cb3 \
                  tmp_aic = tmp_mdl.aic                \
                  \cf2 \cb3 if\cf2 \cb3  tmp_aic < best_aic\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 #se busca aquel con menor AIC: The best-fit model according to AIC is the one that explains \cf2 \cb3 \
                        \cf2 \cb3 #the greatest amount of variation using the fewest possible independent variables.\cf2 \cb3 \
                      best_aic = tmp_aic\
                      best_order = \cf2 \cb3 (\cf2 \cb3 i\cf2 \cb3 ,\cf2 \cb3  d\cf2 \cb3 ,\cf2 \cb3  j\cf2 \cb3 )\cf2 \cb3 \
                      best_mdl = tmp_mdl\
              \cf2 \cb3 except\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 continue\cf2 \cb3 \
  model = sm.tsa.ARIMA\cf2 \cb3 (\cf2 \cb3 train\cf2 \cb3 ,\cf2 \cb3  order=best_order\cf2 \cb3 )\cf2 \cb3 \
  model_fit = model.fit\cf2 \cb3 (\cf2 \cb3 method_kwargs=\cf2 \cb3 \{\cf2 \cb3 "warn_convergence"\cf2 \cb3 :\cf2 \cb3  \cf2 \cb3 False\cf2 \cb3 \})\cf2 \cb3 \
  \cf2 \cb3 return\cf2 \cb3  best_aic\cf2 \cb3 ,\cf2 \cb3  best_order\cf2 \cb3 ,\cf2 \cb3  model_fit\cf2 \cb3 ,\cf2 \cb3  train\cf2 \cb3 ,\cf2 \cb3  test\cf2 \cb3 ,\cf2 \cb3  dates\
\
def arima_rolling(history, test, best_order):\
    predictions = list()\
    for t in range(len(test)):\
        model_fit = sm.tsa.ARIMA(history, order=best_order).fit(method_kwargs=\{"warn_convergence": False\})\
        output = model_fit.forecast() #predicci\'f3n\
        yhat = output[0]\
        predictions.append(yhat)\
        obs = test[t]\
        history.append(obs)\
        print('predicted=%f, expected=%f' % (yhat, obs))\
    return predictions\
}
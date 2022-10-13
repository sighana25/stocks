{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red70\green137\blue204;\red23\green23\blue23;\red202\green202\blue202;
\red212\green214\blue154;\red140\green211\blue254;\red212\green212\blue212;\red89\green156\blue62;\red167\green197\blue152;
\red194\green126\blue101;\red183\green111\blue179;\red113\green184\blue255;\red70\green137\blue204;\red23\green23\blue23;
\red202\green202\blue202;\red212\green214\blue154;\red140\green211\blue254;\red212\green212\blue212;\red67\green192\blue160;
\red183\green111\blue179;\red113\green184\blue255;\red194\green126\blue101;\red89\green156\blue62;\red167\green197\blue152;
}
{\*\expandedcolortbl;;\cssrgb\c33725\c61176\c83922;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;\cssrgb\c86275\c86275\c86275;\cssrgb\c41569\c66275\c30980;\cssrgb\c70980\c80784\c65882;
\cssrgb\c80784\c56863\c47059;\cssrgb\c77255\c52549\c75294;\cssrgb\c50980\c77647\c100000;\cssrgb\c33725\c61176\c83922;\cssrgb\c11765\c11765\c11765;
\cssrgb\c83137\c83137\c83137;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;\cssrgb\c86275\c86275\c86275;\cssrgb\c30588\c78824\c69020;
\cssrgb\c77255\c52549\c75294;\cssrgb\c50980\c77647\c100000;\cssrgb\c80784\c56863\c47059;\cssrgb\c41569\c66275\c30980;\cssrgb\c70980\c80784\c65882;
}
\margl1440\margr1440\vieww37900\viewh21300\viewkind0
\deftab720
\pard\pardeftab720\sl380\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\cf4 \strokec4  \cf5 \strokec5 forecast_accuracy\cf4 \strokec4 (\cf6 \strokec6 forecast\cf4 \strokec4 , \cf6 \strokec6 actual\cf4 \strokec4 , \cf6 \strokec6 str_name\cf4 \strokec4 )\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3     mape = np.mean\cf7 \strokec7 (\cf4 \strokec4 np.\cf5 \strokec5 abs\cf7 \strokec7 (\cf4 \strokec4 forecast - actual\cf7 \strokec7 )\cf4 \strokec4 /np.\cf5 \strokec5 abs\cf7 \strokec7 (\cf4 \strokec4 actual\cf7 \strokec7 ))\cf4 \strokec4  \cf8 \strokec8 # MAPE\cf4 \cb1 \strokec4 \
\cb3     mae = np.mean\cf7 \strokec7 (\cf4 \strokec4 np.\cf5 \strokec5 abs\cf7 \strokec7 (\cf4 \strokec4 forecast - actual\cf7 \strokec7 ))\cf4 \strokec4                  \cf8 \strokec8 # MAE\cf4 \cb1 \strokec4 \
\cb3     rmse = np.mean\cf7 \strokec7 ((\cf4 \strokec4 forecast - actual\cf7 \strokec7 )\cf4 \strokec4 **\cf9 \strokec9 2\cf7 \strokec7 )\cf4 \strokec4 **\cf9 \strokec9 .5\cf4 \strokec4                \cf8 \strokec8 # RMSE\cf4 \cb1 \strokec4 \
\cb3     mse = np.mean\cf7 \strokec7 ((\cf4 \strokec4 forecast - actual\cf7 \strokec7 )\cf4 \strokec4 **\cf9 \strokec9 2\cf7 \strokec7 )\cf4 \strokec4                     \cf8 \strokec8 # MSE\cf4 \cb1 \strokec4 \
\cb3     df_acc = pd.DataFrame\cf7 \strokec7 (\{\cf10 \strokec10 'MAPE'\cf7 \strokec7 :\cf4 \strokec4  \cf7 \strokec7 [\cf4 \strokec4 mape\cf7 \strokec7 ],\cf4 \cb1 \strokec4 \
\cb3                            \cf10 \strokec10 'MAE'\cf7 \strokec7 :\cf4 \strokec4  \cf7 \strokec7 [\cf4 \strokec4 mae\cf7 \strokec7 ],\cf4 \cb1 \strokec4 \
\cb3                            \cf10 \strokec10 'RMSE'\cf7 \strokec7 :\cf4 \strokec4  \cf7 \strokec7 [\cf4 \strokec4 rmse\cf7 \strokec7 ],\cf4 \cb1 \strokec4 \
\cb3                            \cf10 \strokec10 'MSE'\cf7 \strokec7 :\cf4 \strokec4  \cf7 \strokec7 [\cf4 \strokec4 mse\cf7 \strokec7 ],\cf4 \strokec4  \cb1 \
\cb3                            \cf7 \strokec7 \},\cf4 \cb1 \strokec4 \
\cb3                           index=\cf7 \strokec7 [\cf4 \strokec4 str_name\cf7 \strokec7 ])\cf4 \cb1 \strokec4 \
\cb3     \cf11 \strokec11 return\cf4 \strokec4  df_acc\cb1 \
\
\pard\pardeftab720\sl380\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  \cf5 \strokec5 ARIMA_forecast\cf4 \strokec4 (\cf6 \strokec6 serie_dates\cf4 \strokec4 , \cf6 \strokec6 serie\cf4 \strokec4 , \cf6 \strokec6 n_test\cf4 \strokec4 , \cf6 \strokec6 pq\cf4 \strokec4 , \cf6 \strokec6 d\cf4 \strokec4 )\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl380\partightenfactor0
\cf4 \cb3   n_serie=\cf5 \strokec5 len\cf7 \strokec7 (\cf4 \strokec4 serie\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3   train_size = n_serie - n_test\cb1 \
\cb3   train = serie.iloc\cf7 \strokec7 [:\cf4 \strokec4 train_size\cf7 \strokec7 ]\cf4 \cb1 \strokec4 \
\cb3   test = serie.iloc\cf7 \strokec7 [\cf4 \strokec4 train_size\cf7 \strokec7 :\cf4 \strokec4 train_size + n_test\cf7 \strokec7 ]\cf4 \strokec4  \cb1 \
\cb3   dates = serie_dates.iloc\cf7 \strokec7 [\cf4 \strokec4 train_size\cf7 \strokec7 :\cf4 \strokec4 train_size + n_test\cf7 \strokec7 ]\cf4 \cb1 \strokec4 \
\cb3   best_aic = np.inf\cb1 \
\cb3   best_bic = np.inf\cb1 \
\cb3   best_order = \cf2 \strokec2 None\cf4 \cb1 \strokec4 \
\cb3   best_mdl = \cf2 \strokec2 None\cf4 \cb1 \strokec4 \
\cb3   pq_rng = \cf5 \strokec5 range\cf7 \strokec7 (\cf4 \strokec4 pq\cf7 \strokec7 )\cf4 \strokec4  \cf8 \strokec8 #resagos (autoregresivos)\cf4 \cb1 \strokec4 \
\cb3   d_rng  = \cf5 \strokec5 range\cf7 \strokec7 (\cf4 \strokec4 d\cf7 \strokec7 )\cf4 \strokec4  \cf8 \strokec8 #restar maximo 3 veces (diferenciaci\'f3n)\cf4 \cb1 \strokec4 \
\cb3   \cf11 \strokec11 for\cf4 \strokec4  i \cf12 \strokec12 in\cf4 \strokec4  pq_rng\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 #autoregresivos\cf4 \cb1 \strokec4 \
\cb3       \cf11 \strokec11 for\cf4 \strokec4  d \cf12 \strokec12 in\cf4 \strokec4  d_rng\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 #diferenciaci\'f3n\cf4 \cb1 \strokec4 \
\cb3           \cf11 \strokec11 for\cf4 \strokec4  j \cf12 \strokec12 in\cf4 \strokec4  pq_rng\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 #medias moviles\cf4 \cb1 \strokec4 \
\cb3               \cf11 \strokec11 try\cf7 \strokec7 :\cf4 \cb1 \strokec4 \
\cb3                   tmp_mdl = sm.tsa.ARIMA\cf7 \strokec7 (\cf4 \strokec4 train\cf7 \strokec7 ,\cf4 \strokec4  order=\cf7 \strokec7 (\cf4 \strokec4 i\cf7 \strokec7 ,\cf4 \strokec4 d\cf7 \strokec7 ,\cf4 \strokec4 j\cf7 \strokec7 ))\cf4 \strokec4 .fit\cf7 \strokec7 (\cf4 \strokec4 method_kwargs=\cf7 \strokec7 \{\cf10 \strokec10 "warn_convergence"\cf7 \strokec7 :\cf4 \strokec4  \cf2 \strokec2 False\cf7 \strokec7 \})\cf4 \cb1 \strokec4 \
\cb3                   tmp_aic = tmp_mdl.aic                \cb1 \
\cb3                   \cf11 \strokec11 if\cf4 \strokec4  tmp_aic < best_aic\cf7 \strokec7 :\cf4 \strokec4  \cf8 \strokec8 #se busca aquel con menor AIC: The best-fit model according to AIC is the one that explains \cf4 \cb1 \strokec4 \
\cb3                         \cf8 \strokec8 #the greatest amount of variation using the fewest possible independent variables.\cf4 \cb1 \strokec4 \
\cb3                       best_aic = tmp_aic\cb1 \
\cb3                       best_order = \cf7 \strokec7 (\cf4 \strokec4 i\cf7 \strokec7 ,\cf4 \strokec4  d\cf7 \strokec7 ,\cf4 \strokec4  j\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3                       best_mdl = tmp_mdl\cb1 \
\cb3               \cf11 \strokec11 except\cf7 \strokec7 :\cf4 \strokec4  \cf11 \strokec11 continue\cf4 \cb1 \strokec4 \
\cb3   model = sm.tsa.ARIMA\cf7 \strokec7 (\cf4 \strokec4 train\cf7 \strokec7 ,\cf4 \strokec4  order=best_order\cf7 \strokec7 )\cf4 \cb1 \strokec4 \
\cb3   model_fit = model.fit\cf7 \strokec7 (\cf4 \strokec4 method_kwargs=\cf7 \strokec7 \{\cf10 \strokec10 "warn_convergence"\cf7 \strokec7 :\cf4 \strokec4  \cf2 \strokec2 False\cf7 \strokec7 \})\cf4 \cb1 \strokec4 \
\cb3   \cf11 \strokec11 return\cf4 \strokec4  best_aic\cf7 \strokec7 ,\cf4 \strokec4  best_order\cf7 \strokec7 ,\cf4 \strokec4  model_fit\cf7 \strokec7 ,\cf4 \strokec4  train\cf7 \strokec7 ,\cf4 \strokec4  test\cf7 \strokec7 ,\cf4 \strokec4  dates\cb1 \
\
\pard\pardeftab720\sl380\partightenfactor0
\cf13 \cb14 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 def\cf15  \cf16 arima_rolling\cf15 (\cf17 history\cf15 , \cf17 test\cf15 , \cf17 best_order\cf15 )\cf18 :\cf15 \cb1 \
\cb14     predictions = \cf19 list\cf18 ()\cf15 \cb1 \
\cb14     \cf20 for\cf15  t \cf21 in\cf15  \cf16 range\cf18 (\cf16 len\cf18 (\cf15 test\cf18 )):\cf15 \cb1 \
\cb14         model_fit = sm.tsa.ARIMA\cf18 (\cf15 history\cf18 ,\cf15  order=best_order\cf18 )\cf15 .fit\cf18 (\cf15 method_kwargs=\cf18 \{\cf22 "warn_convergence"\cf18 :\cf15  \cf13 False\cf18 \})\cf15 \cb1 \
\cb14         output = model_fit.forecast\cf18 ()\cf15  \cf23 #predicci\'f3n\cf15 \cb1 \
\cb14         yhat = output\cf18 [\cf24 0\cf18 ]\cf15 \cb1 \
\cb14         predictions.append\cf18 (\cf15 yhat\cf18 )\cf15 \cb1 \
\cb14         obs = test\cf18 [\cf15 t\cf18 ]\cf15 \cb1 \
\cb14         history.append\cf18 (\cf15 obs\cf18 )\cf15 \cb1 \
\cb14         \cf16 print\cf18 (\cf22 'predicted=%f, expected=%f'\cf15  % \cf18 (\cf15 yhat\cf18 ,\cf15  obs\cf18 ))\cf15 \cb1 \
\cb14     \cf20 return\cf15  predictions\cb1 \
}
在bert源码的基础上实现了多分类。

1）指定GPU
https://blog.csdn.net/qq_38451119/article/details/81065675

2)将打印的东西存成日志文件
>>nohup.out 2>&1 &
重定向加后台，nohup.out文件就是重定向后的日志

3）加了一个hooks的参数，让训练的时候每10步就输出一次loss
https://www.cnblogs.com/jiangxinyang/p/10241243.html

4）保存每个epoch训练完的模型
[图片]![图片](https://user-images.githubusercontent.com/61902379/113539101-8aa9ed00-960f-11eb-95e9-efa1af19ac3e.png)
main函数里run_config里加上keep_checkpoint_max=FLAGS.keep_checkpoint_max，这就是设置保存模型个数;train的sh脚本里增加两个输入参数save_checkpoints_steps和keep_checkpoints_max
[图片]![图片](https://user-images.githubusercontent.com/61902379/113539240-e8d6d000-960f-11eb-8dbc-3ead6f5cd872.png)
save_checkpoints_steps =int (训练样本数/batch_size)
你epoch设置为n，你的keep_checkpoin_max就要比n大

5） epoch=10，之前已经训练5轮了，现在改成10也没必要重新训练，接上之前的5轮结果继续训练。
[图片]![图片](https://user-images.githubusercontent.com/61902379/113539384-4bc86700-9610-11eb-81c7-a5cda20ffb6c.png)
init_checkpoin改成你最新的模型结果，就是加载最新的模型结果，然后out_put重建一个文件

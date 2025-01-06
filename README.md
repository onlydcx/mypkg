# mypkg

![test](https://github.com/onlydcx/mypkg/actions/workflows/test.yml/badge.svg)

## 概要

- ROS2のパッケージです。
- マシンのメモリ使用量を取得し、トピックにパブリッシュします。

## ノード

- memory_node
    - ROS2が動作しているマシンのメモリ使用率を取得し、```memory_usage```トピックにパブリッシュします。

## トピック

- memory_usage
    - メモリ使用率をFloat64型で1秒ごとに更新します。

## 使用方法

以下のコマンドで実行します。

```
$ ros2 run mypkg memory_node
```

トピックを表示するには以下のコマンドを実行してください。

```
$ ros2 topic echo memory_usage
```

```
data: 41.4
---
data: 41.4
---
data: 41.4
---
data: 41.4
---
data: 41.3
```

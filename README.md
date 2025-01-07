# mypkg

![test](https://github.com/onlydcx/mypkg/actions/workflows/test.yml/badge.svg)

## 概要

- ROS2のパッケージです。
- マシンのメモリ使用量を取得し、トピックにパブリッシュします。

# テスト環境

- Ubuntu 22.04 LTS
    - ROS2 Humble (Github Actions テスト環境)
- Ubuntu 24.04 LTS
    - ROS2 Jazzy (開発環境)

## ノード

- memory_node
    - ROS2が動作しているマシンのメモリ使用率を取得し、```memory_usage```トピックにパブリッシュします。

## トピック

- memory_usage
    - メモリ使用率をFloat64型(std_msgs/msg/Float64)で1秒ごとに更新します。

## 使用方法

以下のコマンドで実行します。

```
$ ros2 run mypkg memory_publisher
```

トピックを表示するには以下のコマンドを実行してください。

```
$ ros2 topic echo memory_usage
```
出力例
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

# ライセンス

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

© 2025 Rin Hanaoka

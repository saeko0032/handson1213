# 🧪 S2. Azure のリソースをセットアップ

ここでは、以下のステップで Azure のリソースをセットアップします。

- ARM テンプレートを使ってリソース作成
- Azure AI Search: インデックスの作成

## 🔖 ARM テンプレートからリソース作成

以下の `Deploy to Azure` のボタンをクリックすることで、Azure ポータルに遷移して以下のリソースを作成するための画面が開きます。

- Azure AI Search
- Azure Cosmos DB
- Function App および App Service Plan

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fstyokosandbox.blob.core.windows.net%2Farm-templates%2Faoai-workshop-azurechat-v2-template.json)

<br>

表示された画面でセットアップを進めます。以下表を参考に入力して、"Review + create" をクリックします。

No. | パラメーター名 | 値
--- | --- | ---
1 | サブスクリプション | ご利用の Azure サブスクリプションを選択します。
2 | リソースグループ | 既存のリソースグループを選択、または新規に作成します。
3 | Code_name | 任意のコードネームを小文字の英語と数字のみで入力します。リソース名の一部として使われます。

![image](./images/s2-1.png)

<br>

"Review + create" をクリックすると、確認画面が表示されます。"Create" をクリックしてリソースの作成を開始します。

リソースの作成には数分かかります。リソースの作成が完了すると、以下の画面が表示されます。

![image](./images/s2-2.png)

<br>

## 🔖 AI Search: インデックスの作成

今回の利用するデータは、Azure のサービスの説明文です。このデータを検索するために必要な検索インデックスのスキーマを定義します。

まず、Auzre portal で AI Search のリソースを表示し、概要の上部にある "インデックスの追加" > "インデックスの追加" をクリックします。

![image](./images/1-2-1.png)

<br>

インデックスの作成画面が表示されます。インデックス名に「azure」と入力します。

![images](./images/1-2-2.png)

<br>

次に "フィールドの追加" をクリックしてフィールドを追加します。以下図を参考に3つのフィールドを追加します。

フィールド名 | 型 | 取得可能 | フィルター可能 | ソート可能 | ファセット可能 | 検索可能 | アナライザー
--- | --- | :---: | :---: | :---: | :---: | :---: | ---
title | Edm.String | ✅ | - | - | - | ✅ | 日本語 - Microsoft
category | Edm.String | ✅ | ✅ | - | - | ✅ | 日本語 - Microsoft
content | Edm.String | ✅ | - | - | - | ✅ | 日本語 - Microsoft

<br>

最後に、ベクターの値を格納するためのフィールドを追加します。入力は以下図を参考に、「フィールド名」「型」「ディメンション」を入力します。  
入力後「ベクター検索プロファイルがありません」の表記の下にある "作成" をクリックします。

![image](./images/1-2-3.png)

<br>

ベクタープロファイルの作成画面が表示されます。今回は、下部にある **"ベクター化"は不要なので作成しません。**  
上部にある**アルゴリズムの構成** の "作成" をクリックします。

![image](./images/1-2-4_1.png)


以下図の画面が表示されますのでデフォルトの値のままで "保存" をクリックします。

> ※ この値に関してご興味がありましたら、以下のドキュメントをご参照ください。
>
> - [ベクター検索の概念 | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/search/vector-search-overview#why-use-vector-search)

![image](./images/1-2-4_2.png)


ベクタープロファイルの画面が表示されます。ベクター化なしのままで、"保存" をクリックします。

![image](./images/1-2-4_3.png)

インデックスフィールドの画面に戻るので、もう一度 "保存" をクリックします。これでこのフィールドの追加が完了です。

<br>

最終的に以下のようなインデックスを構成したことを確認して左下の "作成" をクリックします。

![image](./images/1-2-5.png)

<br>

## 📚 参考情報

### Azure AI Search

- [Azure AI Search の概要 | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/search/search-what-is-azure-search)
- [Azure AI Search のインデックス | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/search/search-what-is-an-index)

<br>

## ⏭️ NEXT STEP ✨

おめでとうございます🎉。ワークショップで利用するすべての Azure のリソースの準備が完了しました。次はコードの実装に進みます。

[⏮️ 前へ](./setup-azure-openai.md) | [📋 目次](../README.md) | [⏭️ 次へ](./setup-function-app-code.md)

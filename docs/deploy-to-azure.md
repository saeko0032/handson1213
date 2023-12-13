# 🧪 (オプション) D5. Azure へのデプロイ: Function App

ここでは、実装した handson-app を Azure 上の Function App へデプロイして、クラウド上で正常に動作することを確認します。

## 🔖 VS Code の拡張機能を使ったデプロイ

今回は VS Code の拡張機能を使ってデプロイと、環境変数の更新を行います。具体的なデプロイ方法は、以下のドキュメントを参考にしてください。

- 参考: [プロジェクト ファイルのデプロイ (Visual Studio Code を使用して Azure Functions を開発する) | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/azure-functions/functions-develop-vs-code?tabs=node-v3%2Cpython-v2%2Cisolated-process&pivots=programming-language-python#republish-project-files)

## 🔖 Azure での動作確認

REST.http を使ってデプロイした API にアクセスし正しく動作することを確認します。

確認するポイントは以下です。

- ✅ デプロイした Function App 上の data_ingestor の API をコールし、Cosmos DB にデータが追加されることを確認
  - Azure portal で Function App のリソースから、各関数の URL を確認できます。
- ✅ AI Search のインデックスが更新されることを確認
- ✅ chat_app の API をコールし、想定されたレスポンスが返ってくることを確認

<br>

## 📚 参考情報

このワークショップでは VS Code から Azure からデプロイを行ないましたが、エンタープライズアプリケーションでは、GitHub Actions や Azure Pipelines を使った CI/CD の自動化が推奨されます。参考までに CI/CD を構成するための情報を記載します。

- [GitHub Actions を使用した継続的デリバリー | Micorosft Learn](https://learn.microsoft.com/ja-jp/azure/azure-functions/functions-how-to-github-actions?tabs=linux%2Cdotnet&pivots=method-template)
- [Azure Pipelines を使用した継続的デリバリー | Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/azure-functions/functions-how-to-azure-devops?tabs=csharp%2Cyaml&pivots=v2)


<br>

---

[📋 目次](../README.md) | [⏮️戻る: data_ingestor.py の実装](./implement-data-ingestor.md)

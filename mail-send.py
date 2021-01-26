{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import smtplib,sys\n",
    "import pandas as pd\n",
    "from email.mime.text import MIMEText\n",
    "from email.utils import formatdate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 送信先のメールリストをCSVフォイルで読み込み\n",
    "\n",
    "elist = pd.read_csv(\"./###.csv\") # CSVファイル名を入力\n",
    "elist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "address_li = elist.email\n",
    "username_li = elist.username\n",
    "number = username_li.size\n",
    "\n",
    "FROM_ADDRESS = '# 自身のメールアドレス'\n",
    "MY_PASSWORD = '# 自身のメールアドレスパスワード'\n",
    "SUBJECT = '忠告！' # 件名を入力"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# メール文の各部分設定\n",
    "\n",
    "def create_msg(from_addr, to_addr, ubject, body):\n",
    "    msg = MIMEText(body)\n",
    "    msg['Subject'] = subject\n",
    "    msg['From'] = from_addr\n",
    "    msg['To'] = to_addr\n",
    "    msg['Date'] = formatdate()\n",
    "    \n",
    "    return msg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# メース送受信のポート設定\n",
    "\n",
    "def send_msg(from_addr, to_addr, msg):\n",
    "    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)\n",
    "    smtpobj.ehlo()\n",
    "    smtpobj.starttls()\n",
    "    smtpobj.ehlo()\n",
    "    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)\n",
    "    smtpobj.sendmail(from_addr, to_addr, msg.as_string())\n",
    "    smtpobj.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "マツムラ\n",
      "0\n",
      "送信完了しました。\n",
      "マサノリ\n",
      "1\n",
      "送信完了しました。\n"
     ]
    }
   ],
   "source": [
    "# メール本文の作成\n",
    "\n",
    "for i in range(number):\n",
    "    BODY = \"\"\"{0}様\n",
    "    お世話になっております。\n",
    "    お金を払ってください。\n",
    "    \"\"\".format(str(username_li[i])) # メール本文を作る\n",
    "    subject = SUBJECT\n",
    "    body = BODY\n",
    "    to_addr = address_li[i]\n",
    "    msg = create_msg(FROM_ADDRESS, to_addr, subject, body)\n",
    "    send_msg(FROM_ADDRESS, to_addr, msg)\n",
    "    \n",
    "    print(username_li[i])\n",
    "    print(i)\n",
    "    print(\"送信完了しました。\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

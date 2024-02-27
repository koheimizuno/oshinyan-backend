register_email = """
    <h3>{}様</h3>
    <h4>
      「推しニャン」サイト事務局ですにゃ。
      <br />
      このたびは、「推しニャン」サイトへの会員登録ありがとうございますにゃ！
    </h4>
    <p style="font-size: 14px">
      推しニャンサイトは、『 お気に入りの看板猫が探せる！推せるサイト』 にゃー。
      <br />
      是非、サイトの中で自分のお気に入りの看板猫を探してにゃ。
    </p>
    <p style="font-size: 14px">
      おうちの周りのお店に、看板猫さんがいたら是非登録をお願いしますにゃ。
      <br />
      それでは、推しニャンサイトをログイン後お楽しみくださいにゃ。
    </p>
    <div>
      <h4 style="margin: 5px">ログイン画面</h4>
      <a href="http://162.43.50.92/login/">https://oshinyan.love/login/</a>
    </div>
    <div>
      <h4 style="margin: 5px">「推しニャン」サイト事務局より</h4>
      <span>
        お問い合わせ先：<a href="mailto:nyan@oshinyan.love"
          >nyan@oshinyan.love</a
        >
      </span>
    </div>
    <p style="font-size: 14px">
      ♡♡♡♡♡♡♡♡♡♡♡♡♡<br />
      推しニャンアンバサダー募集<br />
      にゃんこ好きな方には、アンバサダーになってください。<br />
      きっといいことがあります♪<br />
      <h5 style="margin: 5px">登録はこちら↓</h5>
      <a href="http://162.43.50.92/ambassador/"
        >https://oshinyan.love/ambassador/</a
      >
      <br />
      ♡♡♡♡♡♡♡♡♡♡♡♡♡
    </p>
"""

password_reset_email = """
    <h4>以下のリンクをクリックし、パスワードをリセットしてください。 </h4>
    <p><a href='{0}/password_reset/{1}/{2}'>https://oshinyan.love/password_reset/{1}/{2}</a></p>
"""

unregister_shop_email = """
    <h3>{}様</h3>
    <h4>
      「推しニャン」サイト事務局です。<br />
      看板猫を発見してくれたとのこと！嬉しい限りにゃーー！
    </h4>
    <p style="font-size: 14px">
      このご縁を感謝するにゃーーー！<br />
      事務局の担当にゃんこが情報を確認して、推しニャンサイトに掲載手続きに進むにゃ！
    </p>
    <p style="font-size: 14px">
      「推しニャン」サイトを盛り上げてくれていること、本当に嬉しいにゃん。<br />
      感謝感謝にゃーーーー。
    </p>
    <p>
      <h4 style="margin: 5px">「推しニャン」サイト事務局より</h4>
      <span style="font-size: 14px">お問い合わせ先：<a href="mailto:nyan@oshinyan.love">nyan@oshinyan.love</a></span>
    </p>
    <p style="font-size: 14px">
      ♡♡♡♡♡♡♡♡♡♡♡♡♡<br />
      推しニャンアンバサダー募集<br />
      にゃんこ好きな方には、アンバサダーになってください。<br />
      きっといいことがあります♪<br />
      <h5 style="margin: 5px">登録はこちら↓</h5>
      <a href="http://162.43.50.92/ambassador/"
        >https://oshinyan.love/ambassador/</a
      >
      <br />
      ♡♡♡♡♡♡♡♡♡♡♡♡♡
    </p>
"""

unregister_shop_admin_email = """
    <p>事務局担当者</p>
    <p>
        「推しニャン」サイトに看板猫発見の依頼がありました。<br/>
        下記ご確認ください。
    </p>
    <p>日時：{}</p>
    <p>
        <span>店舗名：{}</span><br />
        <span>メールアドレス：{}</span><br />
        <span>電話：{}</span><br />
        <span>店舗許諾：{}</span><br />
        <span>看板猫情報：{}</span>
    </p>
    <p>以上です。</p>
"""

ambassador_email = """
    <h3>{}様</h3>
    <h4>
        「推しニャン」サイト事務局です。<br>
        このたびは、「推しニャン」アンバサダーへの会員登録ありがとにゃ！
    </h4>

    <p style="font-size: 14px">
        このご縁を感謝するにゃーーー！<br />
        事務局の担当にゃんこから、ご登録のアドレスに個別にご連絡させていただきます。
    </p>

    <p style="font-size: 14px">
        一緒に、「推しニャン」サイトを盛り上げていってもらえること、楽しみにしております。
    </p>

    <p>
      <h4 style="margin: 5px">「推しニャン」サイト事務局より </h4>
        お問い合わせ先：<a href="mailto:nyan@oshinyan.love">nyan@oshinyan.love</a>
    </p>
"""

ambassador_admin_email = """
    <h4>事務局担当者</h4>
    <h5>
      「推しニャン」サイトにアンバサダー登録がありました。 下記ご確認ください。
    </h5>
    <div style="display: flex; align-items: center">
      <h4 style="margin: 5px">日時：</h4>
      <p style="margin: 5px">{}</p>
    </div>
    <div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">アンバサダー名 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">氏名 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">都道府県 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">メールアドレス :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">電話 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">希望 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
    </div>
"""

inquiry_admin_email = """
    <h4>事務局担当者</h4>
    <h5>「推しニャン」サイトに問い合わせが入りました。対応をお願いします。</h5>
    <div style="display: flex; align-items: center">
      <h4 style="margin: 5px">日時：</h4>
      <p style="margin: 5px">{}</p>
    </div>
    <h4>【受理した内容】</h4>
    <div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">問い合わせ種別 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">個人／法人 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">会社名 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">氏名 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">ふりなが :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">電話番号 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">メールアドレス :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">お問い合わせ内容 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
    </div>
    <p>以上です。</p>
"""

inquiry_email = """
    <h3>{}様</h3>
    <h4>
        「推しニャン」サイト事務局です。<br/>
        このたびは、「推しニャン」サイトへのお問い合わせありがとうございます。
    </h4>
    <div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">問い合わせ種別 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">個人／法人 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">会社名 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">氏名 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">ふりなが :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">電話番号 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">メールアドレス :</h5>
        <p style="margin: 5px">{}</p>
      </div>
      <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">お問い合わせ内容 :</h5>
        <p style="margin: 5px">{}</p>
      </div>
    </div>
    <p style="font-size: 14px">
      いただいた内容は、事務局にて返信内容等を精査させていただき、ご連絡が必要と思われたもののみ別途ご連絡をさせていただきます。
    </p>
    <p>
      <h4 style="margin: 5px">「推しニャン」サイト事務局より </h4>
        お問い合わせ先：<a href="mailto:nyan@oshinyan.love">nyan@oshinyan.love</a>
    </p>
"""

report_email = """
    <h4>事務局担当者</h4>
    <h5>
    「推しニャン」サイトにユーザーから通報がありました。対応をお願いします。
    </h5>
    <div style="display: flex; align-items: center">
    <h4 style="margin: 5px">日時：</h4>
    <p style="margin: 5px">{}</p>
    </div>
    <h4>【受理した内容】</h4>
    <div>
    <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">店舗名 :</h5>
        <p style="margin: 5px">{}</p>
    </div>
    <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">通報URL :</h5>
        <p style="margin: 5px">{}</p>
    </div>
    <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">氏名 :</h5>
        <p style="margin: 5px">{}</p>
    </div>
    <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">ふりなが :</h5>
        <p style="margin: 5px">{}</p>
    </div>
    <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">電話番号 :</h5>
        <p style="margin: 5px">{}</p>
    </div>
    <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">メールアドレス :</h5>
        <p style="margin: 5px">{}</p>
    </div>
    <div style="display: flex; align-items: center">
        <h5 style="margin: 5px">お問い合わせ内容 :</h5>
        <p style="margin: 5px">{}</p>
    </div>
    </div>
    <p>以上です。</p>
"""
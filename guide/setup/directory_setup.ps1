# フォルダ作成
$dirs = @(
    'study\math\notebook',
    'study\japanese\重要表現まとめ',
    'study\japanese\notebook',
    'study\english\重要表現まとめ',
    'study\english\notebook',
    'study\science\重要語句まとめ',
    'study\science\notebook',
    'study\social\geography\notebook',
    'study\social/history\notebook',
    'study\social/economy\notebook',
    'study\info'
)

foreach ($d in $dirs) {
    New-Item -ItemType Directory -Path $d -Force | Out-Null
}

# 空ファイル作成
$files = @(
    'study\math\公式まとめ.md',
    'study\math\textbook-data.md',
    'study\math\notebook\2026-02-16.md',

    'study\japanese\textbook-data.md',
    'study\japanese\notebook\2026-02-16.md',
    'study\japanese\重要表現まとめ\古文.md',
    'study\japanese\重要表現まとめ\漢文.md',
    'study\japanese\重要表現まとめ\その他.md',

    'study\english\textbook-data.md',
    'study\english\notebook\2026-02-16.md',
    'study\english\重要表現まとめ\grammar.md',
    'study\english\重要表現まとめ\reader.md',
    'study\english\重要表現まとめ\others.md',

    'study\science\textbook-data.md',
    'study\science\notebook\2026-02-16.md',
    'study\science\重要語句まとめ\biology.md',
    'study\science\重要語句まとめ\chemistry.md',

    'study\social\geography\textbook-data.md',
    'study\social\geography\notebook\2026-02-16.md',

    'study\social\history\textbook-data.md',
    'study\social\history\notebook\2026-02-16.md',

    'study\social\economy\textbook-data.md',
    'study\social\economy\notebook\2026-02-16.md',

    'study\info\textbook-data.md'
)

foreach ($f in $files) {
    New-Item -ItemType File -Path $f -Force | Out-Null
}

Write-Host "Studyディレクトリ構造が作成されました！"

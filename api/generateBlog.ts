// api/generateBlog.ts
import type { VercelRequest, VercelResponse } from '@vercel/node';

export default function handler(req: VercelRequest, res: VercelResponse) {
  const { keyword = '' } = req.body ?? {};
  res.status(200).json({
    title: `${keyword} を極めるバイオハック入門`,
    outline: '- 導入\n- 問題提起\n- 解決策\n- まとめ'
  });
}


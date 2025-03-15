using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;

public class AnimatorController : MonoBehaviour
{
    //操作したいAnimationControllerを持ったGameObjectを割り当てる
    public Animator animator;
    private FileSystemWatcher watcher;

    // Start is called before the first frame update
    void Start()
    {
        watcher = new FileSystemWatcher();
        watcher.Path = @"C:\Users\kajiwara\Documents\AITuber\output"; // 監視するディレクトリを設定
        watcher.Filter = "emotion.txt"; // テキストファイルのみを監視
        watcher.Changed += OnChanged; // ファイルが変更されたときのイベントハンドラを設定
        
        watcher.EnableRaisingEvents = true; // イベントを有効にする
    }

    // Update is called once per frame
    void Update()
    {

    }

    private static void OnChanged(object source, FileSystemEventArgs e)
    {
        // ファイルが変更されたときにその内容を読み取る
        string contents = File.ReadAllText(e.FullPath);
        Debug.Log($"File: {e.FullPath} {e.ChangeType}");
        Debug.Log(contents);

        // ファイルの内容によってアニメーションを変更する
        // ChangeAnimation(contents);
    }

    public void ChangeAnimation(string emotion)
    {
        // Bool
        if(emotion == "0")
        {
            animator.SetBool("Run", false);
            animator.SetBool("Jump", true);
        } 
        if(emotion == "1")
        {
            animator.SetBool("Jump", false);
            animator.SetBool("Run", true);
        }
    }
}

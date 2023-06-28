



class Video {
    constructor (title, uploader , time) {
        this.title = title
        this.uploader = uploader 
        this.time = time
    }
    
    watch () {
        console.log(`${this.uploader} watched all ${this.time} secondes of ${this.title}`)
    }
}  

const videoSplit = new Video("Split", "Michael", 5200)
const newVid = new Video("Shutter Island", "Michael", 5600)
newVid.watch()
videoSplit.watch()


const videosArray = [
    {
        title: "6th Sens",
        uploader: "Marc",
        time: 6000
    },
    {
        title: "The Village",
        uploader: "Paul",
        time: 6200
    },
    {
        title: "Princess Mononoke",
        uploader: "Michael",
        time: 5900
    },
    {
        title: "Blade Runner",
        uploader: "Michael",
        time: 6600
    },
    {
        title: "Titanic",
        uploader: "Suzan",
        time: 6800
    }
]

videosArray.forEach((element)=>{
    new Video(element.title, element.uploader, element.time).watch();
    
})


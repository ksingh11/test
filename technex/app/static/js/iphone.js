var iPhoneAnimation = function(){
	var initialPosition = null;
	var previousPosition = {};
	var direction = "";
	var width = parseInt($(".content-box:first").width(), 10);
	var thirdWidth = parseInt(width / 80, 10);
	
	return {
		init: function(){
			this.panalIndicators(0);
		},
		moveInfo: function(e){
			var $this = $(this);
			
			//Correct position in current box
			var position = e.pageX - $("#wrapper").offset().left;
			
			//Set our initial position, mouse movement now relates to this point
			if(initialPosition === null){initialPosition = {left: position};}
			
			//Relative mouse point
			var mouseToPoint = initialPosition.left - position;
			
			//Check what direction mouse moved
			if(position > previousPosition.left){
				direction = "right";
			} else if(position < previousPosition.left){
				direction = "left";
			}
			previousPosition = {left: position};
			
			//Move the current container to point
			$this.css({
				marginLeft: -mouseToPoint
			});
		},
		panelAnimate: function($this){
			//Grab margin the panel was pulled too
			var margin = parseInt($this.css("marginLeft"), 10);
			
			//Look see if there is a previous / next element
			var $next = $this.next();
			var $prev = $this.prev();
			
			//Index used in indicators
			var index = $this.index();
			
			//User pulled left
			if(direction === "left"){
				//We have a next element to show
				if($next.length && margin < -thirdWidth){
					$this.animate({
						marginLeft: -width
					}, 550, "easeOutCirc");
					//Animated, now change indicator
					this.panalIndicators(index + 1);
				} else {
					//Spring back
					$this.animate({
						marginLeft: 0
					}, 550, "easeOutCirc");
				}
			}
			
			//User pulled right
			if(direction === "right"){
				//We have a previous element to show
				if($prev.length && margin > thirdWidth){
					$prev.animate({
						marginLeft: 0
					}, 550, "easeOutCirc", function(){
						$this.css({
							marginLeft: 0
						});
					});
					//Animated, now change indicator
					this.panalIndicators(index - 1);
				} else {
					//Spring back
					$this.animate({
						marginLeft: 0
					}, 550, "easeOutCirc");
				}
			}
		},
		panalIndicators: function(index){
			//Create our panal indicators
			if(!$("#panelIndicator").length){
				var indHTML = "<ol id='panelIndicator'>";
				$(".content-box", document.getElementById("fake")).each(function(){
					indHTML += "<li>&bull;</li>";
				});
				indHTML += "</ol>";
				//Modify before hitting the DOM
				var $modified = $(indHTML).find("li:first").addClass("active").end();
				
				//Append to the wrapper
				$("#wrapper").append($modified);
			}
			//Remove active
			$("#panelIndicator").find("li").removeClass("active").end().find("li:eq(" + index + ")").addClass("active");
		},
		resetVars: function(){
			initialPosition = null;
		}
	};
}();

jQuery(function($){
	//Initialise
	iPhoneAnimation.init();
	
	//Mouse down bind move event
	$(".content-box").bind("mousedown", function(e){
		$(this).bind("mousemove", iPhoneAnimation.moveInfo);
	});
	
	//Unbind mouse event
	$(".content-box").bind("mouseup", function(e){
		var $this = $(this);
		
		$this.unbind("mousemove", iPhoneAnimation.moveInfo);
		//Animate the panel
		iPhoneAnimation.panelAnimate($this);
		//Reset the private var
		iPhoneAnimation.resetVars();
	});
});

/*Function: Returns the index of the Panel currently displayed.
 Author: Pranjal */
function currpanelind(){
    var i=0, j=0;
    for(i=0; i<=7; i++){
        j = $(".content-box").eq(i).offset().left;
        if (j == 0){
            break;
        }
    }
    // The value of i at this point will give the index of that content-box element which is currently on screen.
    return i;
}

var sliden=1;
var stym=100;
 //sliden n indiactes no. of panels to slide. (defined by Pranjal)
/*Function: Slides screen by no. of panels  passed as a parameter.
 Author: Pranjal */
function slidebyn(sliden,stym)
{
    if (sliden >0)
    {
        sliden--;
        var i=0;
        i=currpanelind();
        //Slide the screen to the appropriate panel with recursive callback to the same fn. later.
        var panelwidthx = parseInt($(".content-box:first").width(), 10);
        $(".content-box").eq(i).animate({marginLeft: -(panelwidthx)},100, function(){
        // recursively calling sliden() till no. of slides desired is achieved
        if (sliden!=0) {
            slidebyn(sliden);
        }
        setpindicator();
        });
    } //End Outer if

    if (sliden < 0)
    {
        sliden++;
        var i=0;
        i=currpanelind();
        var obj = $(".content-box").eq(currpanelind()-1);
        obj.animate({marginLeft: 0}, 100, "easeOutCirc", function(){
            //obj.css({marginLeft: 0},stym,function(){

            // recursively calling sliden() till no. of slides desired is achieved
            if (sliden!=0)
                {slidebyn(sliden);
                }
            setpindicator();
            //});
        });
    } //End Outer if

    return 0;
} //End slidebyn()

var gotopanel = 0;
/*Function: Goes to the desired panel index from current.
 Author: Pranjal */
 
function panelswitch(gotopanel,slidetime)
{
    var cid=currpanelind();
    gotopanel = gotopanel - cid ;
    slidebyn(gotopanel,slidetime); //slidetime maybe redundant
}

/*Function to make the correct panel indicator active
 Author: Pranjal */
function setpindicator(){
    $("#panelIndicator").delay(stym).find("li").removeClass("active").end().find("li").eq(currpanelind()).addClass("active");
}

/*Function to load correct panel of index page from other html file
 Author: Pranjal  */
 
var ploadindex=0;
function loadkaro(ploadindex){

    //$(
    document.location.pathname="/tp4";
    //$.('index.html', function() {
      
    //  panelswitch(ploadindex);
    //});

}